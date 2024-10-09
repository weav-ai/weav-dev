# python3 documents/documents/create_folder.py --name "new folder" --category "" --description ""

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType
from documents.service import FolderOperations
from documents.models import CreateFolderRequest
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    folder_operation = FolderOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--name", type=str, required=True, help="Name of the folder to be created"
    )
    parser.add_argument(
        "--category",
        type=str,
        default="",
        required=False,
        help="The category of the entire folder",
    )
    parser.add_argument(
        "--description",
        type=str,
        default="",
        required=False,
        help="A description for the folder",
    )

    args = parser.parse_args()

    data = CreateFolderRequest(
        name=args.name, category=args.category, description=args.description
    )
    folder_create_response = folder_operation.create_folder(folder_request=data)
    print(folder_create_response.model_dump())
