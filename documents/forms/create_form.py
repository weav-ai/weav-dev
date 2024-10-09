# python3 documents/forms/create_form.py --name "new form" --category "new" --description "test" --is_shared true --is_searchable true --fields "[{\n  \"name\": \"MICROSOFT FORM\",\n  \"description\": \"A form for microsoft\",\n  \"category\": \"ANNUAL REPORT\",\n  \"fields\": [\n    {\n      \"name\": \"Cost of revenue\",\n      \"field_type\": \"Number\",\n      \"is_array\": false,\n      \"fill_by_search\": false,\n      \"description\": \"Extract cost of revenue\"\n    }\n  ],\n  \"is_searchable\": false,\n  \"is_shared\": false\n}]"

import sys
import os
import argparse
import json

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
        "--description", type=str, default="", required=False, help="Form description"
    )
    parser.add_argument(
        "--is_shared",
        type=str,
        choices=BOOL_CHOICES,
        default="False",
        required=False,
        help="Sharing mode",
    )
    parser.add_argument(
        "--is_searchable",
        type=str,
        default="False",
        choices=BOOL_CHOICES,
        required=False,
        help="Whether to search field from the internet",
    )

    parser.add_argument(
        "--fields",
        type=str,
        default="[]",
        required=False,
        help="Form fields",
    )

    args = parser.parse_args()
    try:
        form_fields = json.loads(args.fields)
    except:
        raise Exception("Invalid data in fields")

    body = CreateFormRequest(
        name=args.name,
        description=args.description,
        category=args.category,
        is_shared=get_bool_value(args.is_shared),
        is_searchable=get_bool_value(args.is_searchable),
        fields=form_fields,
    )
    form_create_response = form_operation.create_form(form_data=body)
    pprint(form_create_response.model_dump())
