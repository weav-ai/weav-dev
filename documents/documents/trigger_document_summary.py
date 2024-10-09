# python3 documents/documents/trigger_document_summary.py --document_id 66ff1732927ce8c0ebda42bd

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
        help="Document ID",
    )

    args = parser.parse_args()

    document_summary_response = document_operation.trigger_document_summary(
        document_id=args.document_id,
    )
    pprint(document_summary_response.model_dump())
