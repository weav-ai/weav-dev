# python3 documents/forms/create_form.py --name "new form" --category "new" --description "test" --is_shared true --is_searchable true

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType, BOOL_CHOICES, get_bool_value
from documents.service import FormOperations
from documents.models import CreateFormRequest
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    form_operation = FormOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument("--name", type=str, required=True, help="Form name")
    parser.add_argument("--category", type=str, required=True, help="Form category")
    parser.add_argument(
        "--description", type=bool, default=False, help="Form description"
    )
    parser.add_argument(
        "--is_shared",
        type=str,
        choices=BOOL_CHOICES,
        default=False,
        required=False,
        help="Sharing mode",
    )
    parser.add_argument(
        "--is_searchable",
        type=str,
        choices=BOOL_CHOICES,
        required=True,
        help="Visibilty mode",
    )

    args = parser.parse_args()

    body = CreateFormRequest(
        name=args.name,
        description=args.description,
        category=args.category,
        is_shared=get_bool_value(args.is_shared),
        is_searchable=get_bool_value(args.is_searchable),
    )
    form_create_response = form_operation.create_form(form_data=body)
    pprint(form_create_response.dict())
