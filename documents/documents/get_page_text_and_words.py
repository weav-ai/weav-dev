# python3 documents/documents/get_page_text_and_words.py --document_id 66f9ccbb927ce8c0ebda4261 --page_number 1

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType
from documents.service import DocumentOperations
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    document_operation = DocumentOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--page_number", type=str, required=True, help="Page number to be searched"
    )
    parser.add_argument(
        "--document_id",
        type=str,
        required=True,
        help="Document id",
    )

    args = parser.parse_args()

    page_info_response = document_operation.get_page_text_and_words(
        document_id=args.document_id, page_number=args.page_number
    )
    pprint(page_info_response.model_dump())
