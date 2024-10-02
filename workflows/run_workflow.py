# python3 workflows/run_workflow.py --doc_id 66e0fba3089fbd21c4dd80c3 --workflow_name dagtest

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models import WorkflowRequest
from config_models import LoadConfigurations, ServiceType
from service import WorkflowService
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.WORKFLOWS)
    workflows = WorkflowService(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--workflow_name",
        type=str,
        required=True,
        help="Name of workflow",
    )

    parser.add_argument(
        "--doc_id",
        type=str,
        required=True,
        help="Document for which the workflow has to be run",
    )
    parser.add_argument(
        "--data",
        type=dict,
        default={},
        required=False,
        help="The task which needs to be re run",
    )

    args = parser.parse_args()

    single_workflow_response = workflows.run_workflow(
        workflow_name=args.workflow_name,
        data=WorkflowRequest(doc_id=args.doc_id, data=args.data),
    )
    pprint(single_workflow_response.dict())
