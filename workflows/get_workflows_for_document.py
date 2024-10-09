# python3 workflows/get_workflows_for_document.py --doc_id 66fe1752927ce8c0ebda42b9 --state "success" --query "ANNUAL REPORT" --skip 0 --limit 1

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
        "--doc_id",
        type=str,
        required=True,
        help="Document for which the workflow has to be fetched",
    )

    parser.add_argument(
        "--state",
        type=str,
        default="",
        required=False,
        help="State of workflow",
    )

    parser.add_argument(
        "--query",
        type=str,
        default="",
        required=False,
        help="This string is matched with workflow and document name",
    )

    parser.add_argument(
        "--skip",
        type=int,
        default=0,
        required=False,
        help="Number of workflows to skip",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        required=False,
        help="Max fetch size",
    )

    args = parser.parse_args()

    workflow_response = workflows.get_workflow_runs_for_document(
        doc_id=args.doc_id,
        state=args.state,
        query=args.query,
        skip=args.skip,
        limit=args.limit,
    )
    pprint(workflow_response.model_dump())
