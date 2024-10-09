# python3 documents/forms/update_form_definition.py --form_id 66fe234870dd6d497d9b8ba5 --name "UPDATED_NAME" --category "SECURITIES AND EXCHANGE COMMISSION" --description "I just updated the desc" --is_shared True --is_searchable True --fields '[{"name": "Cost of revenue", "field_type": "Number", "is_array": false, "fill_by_search": false, "description": "Extract cost of revenue"}]'

import sys
import os
import argparse
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from documents.models import UpdateFormDefinitonRequest
from config_models import LoadConfigurations, ServiceType, BOOL_CHOICES, get_bool_value
from documents.service import FormOperations
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    form_operation = FormOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument("--form_id", type=str, required=True, help="Form ID")
    parser.add_argument("--name", type=str, required=True, help="Form name")
    parser.add_argument("--category", type=str, required=True, help="Form category")
    parser.add_argument(
        "--description", type=str, required=True, help="Form description"
    )
    parser.add_argument(
        "--is_shared",
        default="False",
        choices=BOOL_CHOICES,
        type=str,
        required=True,
        help="Form share mode",
    )
    parser.add_argument(
        "--is_searchable",
        type=str,
        default="False",
        choices=BOOL_CHOICES,
        required=False,
        help="Allows the field to be searchable on the internet",
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

    args = parser.parse_args()
    body = UpdateFormDefinitonRequest(
        name=args.name,
        category=args.category,
        description=args.description,
        is_shared=get_bool_value(args.is_shared),
        is_searchable=get_bool_value(args.is_searchable),
        fields=form_fields,
    )

    form_update_response = form_operation.update_form_definition(
        form_id=args.form_id, form_data=body
    )
    pprint(form_update_response.model_dump())
