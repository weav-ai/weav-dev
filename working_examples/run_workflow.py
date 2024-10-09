import sys
import os
import argparse
import json
from typing import Optional, Dict, Any

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config_models import LoadConfigurations, ServiceType
from documents.service import DocumentOperations
from workflows.service import WorkflowService
from workflows.models import WorkflowRequest

workflow_configs = LoadConfigurations().set_config(service=ServiceType.WORKFLOWS)
workflow_operation = WorkflowService(configs=workflow_configs)


def get_workflow_status(workflow_id: str, workflow_run_id: str):
    print(
        f"Retrieving workflow status for Workflow {workflow_id}, Run ID {workflow_run_id}"
    )
    return workflow_operation.get_workflow_status(
        workflow_id=workflow_id, workflow_run_id=workflow_run_id
    )


def get_all_workflows():
    response = workflow_operation.get_all_workflows()
    return [workflow.name for workflow in response.workflows]


def run_workflow(
    workflow_name: str, document_id: str, data: Optional[Dict[Any, Any]] = None
):
    if data is None:
        data = {}
    print(f"Running workflow {workflow_name} on {document_id}")
    return workflow_operation.run_workflow(
        workflow_name=workflow_name,
        data=WorkflowRequest(doc_id=document_id, data=data),
    )


def main():
    print("Script to run workflows")
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")
    action_choices = [
        "get_all_workflows",
        "run_workflow",
        "get_workflow_status",
        "rerun_workflow",
    ]

    all_workflows = get_all_workflows()
    parser.add_argument(
        "--action",
        type=str,
        choices=action_choices,
        help="Choose whether to upload or get a document",
    )

    args = parser.parse_args()

    if args.action is None or args.action not in action_choices:
        print(f"No action specified. Please enter one of {action_choices}.")
        parser.print_usage()
        return

    if args.action == "get_all_workflows":
        print("Action selected: Retrieve all workflows")
        response = all_workflows
        print(response)
    elif args.action == "get_workflow_status":
        print("Action selected: Retrieve workflow status")
        workflow_id = input("Enter workflow ID: ")
        workflow_run_id = input("Enter workflow run ID: ")
        response = get_workflow_status(
            workflow_id=workflow_id, workflow_run_id=workflow_run_id
        )
        print(response)
    elif args.action == "run_workflow":
        print("Action selected: Run workflow")
        print("Choose which workflow to run")
        print("Available workflows:")
        print(all_workflows)
        workflow_name = input("Enter workflow name: ")
        if workflow_name not in all_workflows:
            raise ValueError("Workflow does not exist")
        print(f"Selected to run {workflow_name} workflow")
        document_id = input("Enter document ID for which the workflow has to be run: ")
        additional_data = input(
            "Enter any additional parameters to provide to the workflow. Press enter to skip. "
        )
        if additional_data in [None, ""]:
            additional_data = "{}"
        try:
            additional_data = json.loads(additional_data)
        except Exception as ex:
            print(ex)
            print("Invalid additional data. Please check and re-enter")

        response = run_workflow(
            workflow_name=workflow_name, document_id=document_id, data=additional_data
        )
        print(response)
        print(f"Run ID: {response.run_id}")
        print(f"Workflow ID: {response.workflow_id}")


if __name__ == "__main__":
    main()
