# python3 documents/forms/filter_form.py --scope "all_forms" --is_searchable false --query "ANNUAL REPORT"

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType, BOOL_CHOICES, get_bool_value
from documents.service import FormOperations
from documents.models import FilterFormRequest
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    form_operation = FormOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--scope",
        type=str,
        required=True,
        choices=["all_forms", "my_forms"],
        help="Scope of form definition",
    )
    parser.add_argument(
        "--is_searchable",
        required=False,
        type=str,
        choices=BOOL_CHOICES,
        default="false",
        help="When not specified, all are returned.",
    )
    parser.add_argument(
        "--query",
        type=str,
        default="",
        required=False,
        help="This string is matched in category and description",
    )

    args = parser.parse_args()

    body = FilterFormRequest(
        query=args.query,
        scope=args.scope,
        is_searchable=get_bool_value(args.is_searchable),
    )
    form_create_response = form_operation.filter_form(form_data=body)
    pprint(form_create_response.model_dump())
