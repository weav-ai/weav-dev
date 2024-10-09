# python3 documents/forms/delete_form_definition.py --form_id 66ea66d547fff0950cba17e


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

    print("You are about to perform a DELETE operation.")
    confirm = str(input("Are you sure you want to continue? (Y/N): "))
    if confirm.lower() in {"yes", "y"}:
        form_delete_response = form_operation.delete_form_definition(
            form_id=args.form_id
        )
        pprint(form_delete_response.model_dump())
    else:
        print("Cancelled operation.")
