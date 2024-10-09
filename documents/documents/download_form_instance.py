# python3 documents/documents/download_form_instance.py --download_format "JSON" --document_id "66e0f93093798ee1c937"

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType
from documents.service import DocumentOperations

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    document_operation = DocumentOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument("--document_id", type=str, required=True, help="Document ID")
    parser.add_argument(
        "--download_format",
        type=str,
        default="JSON",
        choices=["CSV", "JSON"],
        required=False,
        help="Download format",
    )

    args = parser.parse_args()

    download_form_response = document_operation.download_form_instance(
        document_id=args.document_id, download_format=args.download_format
    )
    print(download_form_response)
