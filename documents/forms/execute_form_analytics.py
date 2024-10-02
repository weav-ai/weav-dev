import sys
import os
import argparse
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType
from documents.service import FormOperations
from documents.models import ExecuteFormAnalyticsRequest

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    form_operation = FormOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument("--form_id", type=str, required=True, help="Form ID")
    parser.add_argument(
        "--skip",
        type=int,
        default=0,
        required=False,
        help="Number of documents to skip",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        required=False,
        help="Total number of documents to consider",
    )

    args = parser.parse_args()

    body = ExecuteFormAnalyticsRequest(
        skip=args.skip,
        limit=args.limit,
    )
    execute_form_analytics_response = form_operation.execute_form_analytics(
        form_id=args.form_id, form_data=body
    )
    pprint(execute_form_analytics_response.dict())
