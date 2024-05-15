from __future__ import annotations

import importlib
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from kgbuilder.models import InputFile


def git_list_files(indir: Path, branch: str = "main") -> list[InputFile]:
    """
    List all files in a git repository
    """
    output = subprocess.check_output(["git", "ls-tree", "-r", branch], cwd=indir)
    content = output.decode().strip().split("\n")
    files = []
    for line in content:
        objectmode, objecttype, objectname, relpath = line.split()
        assert objecttype == "blob"
        files.append(InputFile(relpath=relpath, path=indir / relpath, key=objectname))
    return files


def import_func(func_ident: str) -> Callable:
    """Import function from string, e.g., sm.misc.funcs.import_func"""
    lst = func_ident.rsplit(".", 2)
    if len(lst) == 2:
        module, func = lst
        cls = None
    else:
        module, cls, func = lst
        try:
            importlib.import_module(module + "." + cls)
            module = module + "." + cls
            cls = None
        except ModuleNotFoundError as e:
            if e.name == (module + "." + cls):
                pass
            else:
                raise

    module = importlib.import_module(module)
    if cls is not None:
        module = getattr(module, cls)

    return getattr(module, func)


if __name__ == "__main__":
    git_list_files(Path(__file__).parent.parent.parent / "ta2-minmod-data", "main")
