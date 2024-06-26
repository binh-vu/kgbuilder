import base64
import json
import os
import sys

import jsonschema
import kgbuilder.input_validators.generate_uris as generate_uris
import kgbuilder.input_validators.validator_utils as validator_utils
import requests
import validators


def read_file_from_github(owner, repo, path_to_file, token, branch):
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path_to_file}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)

    # Parse the response JSON
    file_info = ""

    if response.status_code == 200:
        file_info = response.text
    elif response.status_code == 404:
        print(f"File '{file_path}' was deleted, skipping.")
        sys.exit(0)
    else:
        print(f"Failed to read file. Status code: {response.status_code}")
        sys.exit(1)

    return file_info


def validate_json_schema(json_data):

    schema = validator_utils.mineral_site_schema()
    json_string = json.dumps(json_data)
    mineral_site_json = json.loads(json_string)

    try:
        jsonschema.validate(instance=mineral_site_json, schema=schema)
        print("Validation succeeded")
    except jsonschema.ValidationError as e:
        print(f"Validation failed: {e}")
        raise  # Raise an exception to indicate failure

    return json_data


def validate_json_schema_mineral_system(json_data):

    schema = validator_utils.mineral_system_schema()
    json_string = json.dumps(json_data)
    mineral_system_json = json.loads(json_string)

    try:
        jsonschema.validate(instance=mineral_system_json, schema=schema)
        print("Validation succeeded")
    except jsonschema.ValidationError as e:
        print(f"Validation failed: {e}")
        raise  # Raise an exception to indicate failure

    return json_data


def add_id_to_mineral_site(json_data, file_path):
    ms_list = json_data["MineralSite"]
    mndr_url = "https://minmod.isi.edu/resource/"

    for ms in ms_list:
        ms_id = validator_utils.mineral_site(ms)
        ms["id"] = mndr_url + ms_id

        if "deposit_type_candidate" in ms:
            for dp in ms["deposit_type_candidate"]:
                if "normalized_uri" in dp:
                    validator_utils.is_valid_uri(dp["normalized_uri"])
                dp["id"] = mndr_url + validator_utils.deposit_type(dp, ms_id)

        if "location_info" in ms:
            ll = ms["location_info"]
            if "state_or_province" in ll and ll["state_or_province"] is None:
                ll["state_or_province"] = ""

        if "mineral_inventory" in ms:
            mi_list = ms["mineral_inventory"]
            counter = 0

            for mi in mi_list:
                if "category" in mi:
                    for dp in mi["category"]:
                        validator_utils.is_valid_uri(dp)

                if "commodity" in mi:
                    validator_utils.is_valid_uri(mi["commodity"])

                if "ore" in mi:
                    if "ore_unit" in mi["ore"]:
                        ore = mi["ore"]
                        validator_utils.is_valid_uri(ore["ore_unit"])

                if "grade" in mi:
                    if "grade_unit" in mi["grade"]:
                        grade = mi["grade"]
                        validator_utils.is_valid_uri(grade["grade_unit"])

                if "cutoff_grade" in mi:
                    if "grade_unit" in mi["cutoff_grade"]:
                        cutoff_grade = mi["cutoff_grade"]
                        validator_utils.is_valid_uri(cutoff_grade["grade_unit"])

                mi_data = {"site": ms, "id": counter}
                mi["id"] = mndr_url + validator_utils.mineral_inventory(mi_data)
                counter += 1

                if "reference" in mi:
                    reference = mi["reference"]
                    if "document" in reference:
                        document = reference["document"]
                        doc_data = {"document": document}
                        document["id"] = mndr_url + validator_utils.document(doc_data)

    # filename = get_filename(file_path)
    with open(file_path, "w") as file:
        # Write the new data to the file
        file.write(json.dumps(json_data, indent=2) + "\n")
    create_ttl_files.create_drepr_from_mineral_site(file_path)


def add_id_to_mineral_system(json_data, file_path):
    ms_list = json_data["MineralSystem"]
    mndr_url = "https://minmod.isi.edu/resource/"

    for ms in ms_list:
        if "deposit_type" in ms:
            for dp in ms["deposit_type"]:
                validator_utils.is_valid_uri(dp)
        ms["id"] = mndr_url + validator_utils.mineral_system(ms)

        fields = ["source", "pathway", "trap", "preservation", "energy", "outflow"]

        for f in fields:

            if f in ms:
                for f_object in ms[f]:
                    if "supporting_references" in f_object:
                        for reference in f_object["supporting_references"]:
                            if "document" in reference:
                                document = reference["document"]
                                doc_data = {"document": document}
                                document["id"] = mndr_url + validator_utils.document(
                                    doc_data
                                )

    # filename = get_filename(file_path)
    with open(file_path, "w") as file:
        # Write the new data to the file
        file.write(json.dumps(json_data, indent=2) + "\n")
    create_ttl_files.create_drepr_from_mineral_system(file_path)


if __name__ == "__main__":
    changed_files = sys.argv[1]
    temp_file = sys.argv[2]
    token = sys.argv[3]
    branch = sys.argv[4]
    file_path = changed_files

    owner = "DARPA-CRITICALMAAS"
    repo = "ta2-minmod-data"

    if validator_utils.is_json_file_under_data(file_path):
        file_content = read_file_from_github(owner, repo, file_path, token, branch)

        print(f"{file_path} is a JSON file, running validation on it")
        json_data = {}
        try:
            json_string = validator_utils.remove_non_printable_chars(file_content)
            json_data = json.loads(json_string)

            if "MineralSite" in json_data:
                print("Mineral Site validation ...")
                json_data = validate_json_schema(json_data)
            elif "MineralSystem" in json_data:
                print("Mineral System validation ...")
                json_data = validate_json_schema_mineral_system(json_data)
            else:
                print("No validation", json_data)
        except FileNotFoundError:
            print(f"File '{file_path}' was deleted, skipping.")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")
            raise

        json_data = json.loads(json_string)
        print("Json validated ...")

        if "MineralSite" in json_data:
            json_data = add_id_to_mineral_site(json_data, temp_file)
        elif "MineralSystem" in json_data:
            json_data = add_id_to_mineral_system(json_data, temp_file)
    elif validator_utils.is_ttl_file_under_data(file_path):
        file_content = read_file_from_github(owner, repo, file_path, token, branch)
        print(f"{file_path} is a ttl file, running validation on it")
        try:
            create_ttl_files.validate_mineral_site(file_content)
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
    else:
        print(f"{file_path} is not a JSON file")
