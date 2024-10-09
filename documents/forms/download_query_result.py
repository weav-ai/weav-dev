# python3 documents/forms/download_query_result.py --form_id 66f3d44eeb87303bc52bb9b4

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
        "--query",
        default="",
        type=str,
        required=False,
        help="This string is matched in category and description",
    )

    args = parser.parse_args()

    if args.query:
        data = DownloadQueryResultRequest(query=args.query)
    else:
        data = DownloadQueryResultRequest()

    download_query_response = form_operation.download_query_result(
        form_id=args.form_id, download_format=args.download_format, form_data=data
    )
    if args.download_format == "CSV":
        print(download_query_response)
    else:
        pprint(download_query_response.model_dump())
