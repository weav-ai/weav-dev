# python3 documents/folders/get_folder_definition.py --folder_id 66e0f93093798ee1c937e39aent

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType
from documents.service import FolderOperations
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    folder_operation = FolderOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--folder_id",
        type=str,
        required=True,
        help="Unique identifier for the folder",
    )

    args = parser.parse_args()

    folder_definition_response = folder_operation.get_folder_definition(
        folder_id=args.folder_id
    )
    pprint(folder_definition_response.model_dump())
