# python3 documents/forms/get_form_definition.py --form_id 66e9e1ad47fff0950cba17ea


import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType
from documents.service import FormOperations
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    form_operation = FormOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument("--form_id", type=str, required=True, help="Form ID")

    args = parser.parse_args()

    form_definition_response = form_operation.get_form_definition(form_id=args.form_id)
    pprint(form_definition_response.model_dump())
