# python3 workflows/skip_tasks.py --workflow_name "dagtest" --tasks task_1 task_2

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models import SkipStepsInWorkflowRequest
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

    parser.add_argument("--tasks", nargs="+", help="A list of tasks to skip")

    args = parser.parse_args()

    single_workflow_response = workflows.skip_steps_in_workflow(
        workflow_name=args.workflow_name,
        data=SkipStepsInWorkflowRequest(tasks=args.tasks),
    )
    pprint(single_workflow_response.dict())
