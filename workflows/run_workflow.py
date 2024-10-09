# python3 workflows/run_workflow.py --doc_id 66fe5c58b1d0dfb13c9975f3 --workflow_name dagtest

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models import WorkflowRequest
from config_models import LoadConfigurations, ServiceType
from service import WorkflowService
from pprint import pprint
import json

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
        type=str,
        default=r"{}",
        required=False,
        help="Extra parameters for the workflow",
    )

    args = parser.parse_args()
    try:
        data = json.loads(args.data)
    except:
        raise Exception("Invalid data in --data")

    args = parser.parse_args()
    single_workflow_response = workflows.run_workflow(
        workflow_name=args.workflow_name,
        data=WorkflowRequest(doc_id=args.doc_id, data=data),
    )
    pprint(single_workflow_response.model_dump())
