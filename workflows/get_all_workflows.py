# python3 workflows/get_all_workflows.py

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config_models import LoadConfigurations, ServiceType, get_bool_value, BOOL_CHOICES
from service import WorkflowService
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.WORKFLOWS)
    workflows = WorkflowService(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--show_internal_steps",
        type=str,
        choices=BOOL_CHOICES,
        default="false",
        required=False,
        help="Set to true to see all steps",
    )

    args = parser.parse_args()

    all_workflows_response = workflows.get_all_workflows(
        show_internal_steps=get_bool_value(args.show_internal_steps)
    )
    pprint(all_workflows_response.model_dump())
