# python3 documents/documents/get_document_hierarchy.py --document_id 66f9cc39b1d0dfb13c99752a

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
        "--document_id",
        type=str,
        required=True,
        help="Document id",
    )

    args = parser.parse_args()

    document_hierarchy_response = document_operation.get_document_hierarchy(
        document_id=args.document_id
    )
    pprint(document_hierarchy_response.model_dump())
