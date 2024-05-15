from __future__ import annotations

import hashlib
import shutil
from pathlib import Path
from typing import Callable

import orjson
from drepr.main import convert
from hugedict.sqlite import SqliteDict
from kgbuilder.helper import git_list_files, import_func
from kgbuilder.input_validators.generate_file_with_id import generate_file_with_id_main
from kgbuilder.models import FileProcessStatus, InputFile
from loguru import logger
from tqdm.auto import tqdm


class GitBuildPipeline:

    def __init__(self, data_repo_dir: Path, workdir: Path):
        workdir.mkdir(exist_ok=True, parents=True)
        self.validate_cache: SqliteDict[str, FileProcessStatus] = SqliteDict.str(
            workdir / "validate_cache.db",
            ser_value=lambda x: orjson.dumps(x.to_dict()),
            deser_value=lambda x: FileProcessStatus.from_dict(orjson.loads(x)),
        )
        self.build_cache: SqliteDict[str, FileProcessStatus] = SqliteDict.str(
            workdir / "build_cache.db",
            ser_value=lambda x: orjson.dumps(x.to_dict()),
            deser_value=lambda x: FileProcessStatus.from_dict(orjson.loads(x)),
        )
        self.convertors: dict[str, Callable] = {}

        self.data_repo_dir = data_repo_dir

        self.workdir = workdir
        (self.workdir / "logs").mkdir(exist_ok=True)
        self.project_dir = Path(__file__).parent.parent

        self.logger = logger.bind(name=self.__class__.__name__)
        self.logger.add(workdir / "logs/{time}.log", retention="7 days", diagnose=False)

    def step0_prepare_build_env(self):
        infiles = list(self.project_dir.glob("generators/*.yml"))
        self.ensure_no_extra_files(
            {f"{file.stem}.py" for file in infiles},
            self.project_dir / f"kgbuilder/convertors",
        )

        for file in infiles:
            key = hashlib.sha256(file.read_bytes()).hexdigest()
            relpath = str(file.relative_to(self.project_dir))
            outfile = self.project_dir / f"kgbuilder/convertors/{file.stem}.py"
            rebuild = True
            if outfile.exists() and relpath in self.build_cache:
                status = self.build_cache[relpath]
                if status.key == key and status.is_success:
                    rebuild = False

            if rebuild:
                convert(
                    repr=file,
                    resources={},
                    progfile=outfile,
                )
                self.build_cache[relpath] = FileProcessStatus(key=key, is_success=True)
                self.logger.info("[drepr] generate {}", relpath)
            else:
                self.logger.info("[drepr] skip {}", relpath)

            self.convertors[file.stem] = import_func(
                f"kgbuilder.convertors.{file.stem}.main"
            )

    def step1_get_input_files(self) -> list[InputFile]:
        infiles = []
        keep_folders = [
            "data/entities/",
            "data/inferlink/",
            "data/sri/",
            "data/umn/",
            "data/usc/",
        ]
        ignore_folders = [
            "data/umn/archive/",
            "data/umn/raw_databases/",
        ]
        for file in git_list_files(self.data_repo_dir, "main"):
            if any(file.relpath.startswith(p) for p in keep_folders) and not any(
                file.relpath.startswith(p) for p in ignore_folders
            ):
                infiles.append(file)
        return infiles

    def step2_convert_files(self, files: list[InputFile]):
        # ----------- convert predefined entities -----------
        entity_outdir = self.workdir / "entities"
        entity_outdir.mkdir(exist_ok=True, parents=True)

        workfiles = [
            self.assert_valid_file(file)
            for file in files
            if file.relpath.startswith("data/entities/")
            and file.relpath.endswith(".csv")
        ]
        for file in workfiles:
            outfile = entity_outdir / f"{file.path.stem}.ttl"
            rebuild = True
            if outfile.exists() and file.relpath in self.build_cache:
                status = self.build_cache[file.relpath]
                if status.key == file.key and status.is_success:
                    rebuild = False

            if rebuild:
                convertor = {
                    "categories": "categories",
                    "minmod_commodities": "commodities",
                    "minmod_deposit_types": "deposit_types",
                    "minmod_units": "units",
                }[file.path.stem]
                output = self.convertors[convertor](file.path)
                outfile.write_text(output)
                self.build_cache[file.relpath] = FileProcessStatus(
                    key=file.key, is_success=True
                )
                self.logger.info("[entities] convert {}", file.relpath)
            else:
                self.logger.info("[entities] skip {}", file.relpath)

        # ----------- convert same as from umn -----------
        sameas_outdir = self.workdir / "sameas"
        sameas_outdir.mkdir(exist_ok=True, parents=True)

        workfiles = [
            self.assert_valid_file(file)
            for file in files
            if file.relpath.startswith("data/umn/sameas/")
            and file.relpath.endswith(".csv")
        ]
        self.ensure_no_extra_files(
            {f"{file.path.stem}.ttl" for file in workfiles}, sameas_outdir
        )

        for file in workfiles:
            rebuild = True
            outfile = sameas_outdir / f"{file.path.stem}.ttl"
            if outfile.exists() and file.relpath in self.build_cache:
                status = self.build_cache[file.relpath]
                if status.key == file.key and status.is_success:
                    rebuild = False

            if rebuild:
                output = self.convertors["same_as"](file.path)
                outfile.write_text(output)
                self.build_cache[file.relpath] = FileProcessStatus(
                    key=file.key, is_success=True
                )
                self.logger.info("[sameas] convert {}", file.relpath)
            else:
                self.logger.info("[sameas] skip {}", file.relpath)

        # ----------- convert mineral site data -----------
        for team in ["inferlink", "sri", "umn"]:
            team_indir = f"data/{team}"
            if team == "inferlink":
                team_indir += "/extractions"

            team_json_outdir = self.workdir / f"{team}/json"
            team_ttl_outdir = self.workdir / f"{team}/ttl"
            team_json_outdir.mkdir(exist_ok=True, parents=True)
            team_ttl_outdir.mkdir(exist_ok=True, parents=True)

            workfiles = [
                self.assert_valid_file(file)
                for file in files
                if file.relpath.startswith(team_indir)
                and file.relpath.endswith(".json")
                and str(file.path.parent).endswith(team_indir)
            ]
            self.ensure_no_extra_files(
                {f"{file.path.stem}.json" for file in workfiles}, team_json_outdir
            )
            self.ensure_no_extra_files(
                {f"{file.path.stem}.ttl" for file in workfiles}, team_ttl_outdir
            )

            for file in workfiles:
                outfile = team_ttl_outdir / f"{file.path.stem}.ttl"
                rebuild = True
                if outfile.exists() and file.relpath in self.build_cache:
                    status = self.build_cache[file.relpath]
                    if status.key == file.key and status.is_success:
                        rebuild = False

                if rebuild:
                    generate_file_with_id_main(file.path, team_json_outdir)

                    output = self.convertors["mineral_site"](
                        team_json_outdir / file.path.name
                    )
                    outfile.write_text(output)
                    self.build_cache[file.relpath] = FileProcessStatus(
                        key=file.key, is_success=True
                    )
                    self.logger.info("[{}] convert {}", team, file.relpath)
                else:
                    self.logger.info("[{}] skip {}", team, file.relpath)

        # ----------- convert mappable criteria -----------
        mappable_criteria_json_outdir = self.workdir / "mappable_criteria/json"
        mappable_criteria_json_outdir.mkdir(exist_ok=True, parents=True)

        mappable_criteria_ttl_outdir = self.workdir / "mappable_criteria/ttl"
        mappable_criteria_ttl_outdir.mkdir(exist_ok=True, parents=True)

        workfiles = [
            self.assert_valid_file(file)
            for file in files
            if file.relpath.startswith("data/sri/mappableCriteria/")
            and file.relpath.endswith(".json")
        ]
        self.ensure_no_extra_files(
            {f"{file.path.stem}.json" for file in workfiles},
            mappable_criteria_json_outdir,
        )
        self.ensure_no_extra_files(
            {f"{file.path.stem}.ttl" for file in workfiles},
            mappable_criteria_ttl_outdir,
        )

        for file in workfiles:
            outfile = mappable_criteria_ttl_outdir / f"{file.path.stem}.ttl"
            rebuild = True
            if outfile.exists() and file.relpath in self.build_cache:
                status = self.build_cache[file.relpath]
                if status.key == file.key and status.is_success:
                    rebuild = False

            if rebuild:
                generate_file_with_id_main(file.path, mappable_criteria_json_outdir)

                output = self.convertors["mineral_system_v2"](
                    mappable_criteria_json_outdir / file.path.name
                )
                outfile.write_text(output)
                self.build_cache[file.relpath] = FileProcessStatus(
                    key=file.key, is_success=True
                )
                self.logger.info("[mappable_criteria] convert {}", file.relpath)
            else:
                self.logger.info("[mappable_criteria] skip {}", file.relpath)

        # ----------- copy usc -----------
        usc_outdir = self.workdir / "usc"
        usc_outdir.mkdir(exist_ok=True, parents=True)

        workfiles = [
            self.assert_valid_file(file)
            for file in files
            if file.relpath.startswith("data/usc") and file.relpath.endswith(".ttl")
        ]
        self.ensure_no_extra_files(
            {file.path.name for file in workfiles},
            usc_outdir,
        )
        for file in workfiles:
            shutil.copy(file.path, usc_outdir / file.path.name)
            self.logger.info("[usc] copy {}", file.relpath)

    def step3_prepare_output(self, files: list[InputFile]):
        ttl_files = list(self.workdir.glob("**/*.ttl"))

        prefixes = set()
        all_lines = []

        outfile = self.workdir / "all.ttl"
        for ttl_file in tqdm(ttl_files, desc="merge ttl files"):
            if ttl_file == outfile:
                continue

            for line in ttl_file.read_text().splitlines():
                if line.startswith("@prefix "):
                    prefixes.add(line)
                else:
                    all_lines.append(line)

        with open(self.workdir / "all.ttl", "w") as f:
            for line in sorted(prefixes):
                f.write(line + "\n")
            f.write("\n")
            for line in all_lines:
                f.write(line + "\n")

    def run(self):
        try:
            self.step0_prepare_build_env()
            files = self.step1_get_input_files()
            self.step2_convert_files(files)
            self.step3_prepare_output(files)
        except:
            logger.exception("An error occurred")
            raise

    def ensure_no_extra_files(self, expected_filenames: set[str], outdir: Path):
        for file in outdir.glob("*"):
            if file.name not in expected_filenames:
                if file.is_dir():
                    shutil.rmtree(file)
                else:
                    file.unlink()
                self.logger.info("Remove extra file {}", file.name)

    def assert_valid_file(self, file: InputFile) -> InputFile:
        assert len(file.path.name.split(".")) == 2, f"File {file.path} has > 1 `.`"
        return file


if __name__ == "__main__":
    rootdir = Path(__file__).parent.parent.parent
    pipeline = GitBuildPipeline(
        rootdir / "ta2-minmod-data",
        rootdir / "ta2-minmod-kg/data",
    )

    pipeline.run()
