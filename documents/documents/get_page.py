# python3 documents/documents/get_page.py --document_id 66f9ccbb927ce8c0ebda4261 --page_number 1

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType, get_bool_value, BOOL_CHOICES
from documents.service import DocumentOperations
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    document_operation = DocumentOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--page_number", type=str, required=True, help="Page number to be selected"
    )
    parser.add_argument(
        "--document_id",
        type=str,
        required=True,
        help="Document ID",
    )
    parser.add_argument(
        "--bounding_boxes",
        type=str,
        default="false",
        choices=BOOL_CHOICES,
        required=False,
        help="Get information about bounding boxes",
    )

    args = parser.parse_args()

    page_level_status_response = document_operation.get_page(
        document_id=args.document_id,
        page_number=args.page_number,
        bounding_boxes=get_bool_value(args.bounding_boxes),
    )
    pprint(page_level_status_response.model_dump())
