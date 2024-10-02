# python3 documents/forms/download_query_result.py --form_id 66f45d0db1d0dfb13c9974c3 --query "Test query"

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from documents.models import DownloadQueryResultRequest
from config_models import LoadConfigurations, ServiceType
from documents.service import FormOperations
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    form_operation = FormOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument("--form_id", type=str, required=True, help="Form ID")
    parser.add_argument(
        "--download_format",
        type=str,
        default="JSON",
        choices=["JSON", "CSV"],
        required=False,
        help="Download format",
    )
    parser.add_argument(
        "--query", type=str, default="", required=False, help="Search query"
    )

    args = parser.parse_args()

    data = DownloadQueryResultRequest(query=args.query)

    download_query_response = form_operation.download_query_result(
        form_id=args.form_id, download_format=args.download_format, form_data=data
    )
    pprint(download_query_response.dict())
