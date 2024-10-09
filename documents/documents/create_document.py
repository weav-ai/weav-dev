# python3 documents/documents/create_document.py --file_path "folder/path/file.pdf" --folder_id "66e0f93093798ee1c937"

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType
from documents.service import DocumentOperations
from documents.exceptions import DocumentProcessingException
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    document_operation = DocumentOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--file_path", type=str, required=True, help="File path on local"
    )
    parser.add_argument(
        "--folder_id",
        type=str,
        default="",
        required=False,
        help="Folder ID where the document needs to be stored",
    )

    args = parser.parse_args()

    if not os.path.exists(args.file_path):
        raise DocumentProcessingException(
            status_code=404,
            message="File not found, please check file path.",
            response_data="File not found, please check file path.",
        )

    document_create_response = document_operation.create_document(
        file_path=args.file_path, folder_id=args.folder_id
    )
    pprint(document_create_response.model_dump())
