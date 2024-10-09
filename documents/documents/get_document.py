# python3 documents/documents/get_document.py --document_id 66f9ccbb927ce8c0ebda4261 --fill_pages True

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType, BOOL_CHOICES, get_bool_value
from documents.service import DocumentOperations
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    document_operation = DocumentOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--document_id",
        type=str,
        required=True,
        help="Document id",
    )

    parser.add_argument(
        "--fill_pages",
        type=str,
        default="false",
        choices=BOOL_CHOICES,
        required=False,
        help="If false pages will be empty",
    )

    args = parser.parse_args()

    get_document_response = document_operation.get_document(
        document_id=args.document_id, fill_pages=get_bool_value(args.fill_pages)
    )
    pprint(get_document_response.model_dump())
