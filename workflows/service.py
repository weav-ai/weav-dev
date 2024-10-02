# python3 workflows/get_workflow_status.py --workflow_id process_form_workflow --workflow_run_id 66df87ec2b1edfc0dc3b556f_f6328cd2-fbbf-41d0-a756-b111041cae6c

from config_models import ConfigModel, ServiceEndpoints, AUTHENTICATION_FAILED_MESSAGE
from models import (
    GetAllWorkflowsResponse,
    Workflow,
    SkipStepsInWorkflowRequest,
    RunWorkflowResponse,
    WorkflowRequest,
    WorkflowStatusResponse,
)
from exceptions import WorkflowException
import requests


class WorkflowService:
    def __init__(self, configs: ConfigModel):
        self.configs = configs
        self.endpoints = ServiceEndpoints()

    def get_all_workflows(self, show_internal_steps: bool) -> GetAllWorkflowsResponse:
        url = f"{self.configs.base_url}/{self.endpoints.GET_ALL_WORKFLOWS}"
        response = requests.get(
            url=url,
            params=[("show_internal_steps", show_internal_steps)],
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise WorkflowException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise WorkflowException(
                status_code=response.status_code,
                message="Failed to get workflows",
                response_data=response.json(),
            )
        return GetAllWorkflowsResponse(workflows=response.json())

    def get_single_workflow(
        self, workflow_name: str, show_internal_steps: bool
    ) -> Workflow:
        url = f"{self.configs.base_url}/{self.endpoints.GET_SINGLE_WORKFLOW.format(WORKFLOW_NAME=workflow_name)}"
        response = requests.get(
            url=url,
            params=[("show_internal_steps", show_internal_steps)],
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise WorkflowException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise WorkflowException(
                status_code=response.status_code,
                message=f"Failed to get workflow {workflow_name}",
                response_data=response.json(),
            )

        return Workflow.parse_obj(response.json())

    def skip_steps_in_workflow(
        self, workflow_name: str, data: SkipStepsInWorkflowRequest
    ) -> Workflow:
        url = f"{self.configs.base_url}/{self.endpoints.SKIP_TASK_IN_WORKFLOW.format(WORKFLOW_NAME=workflow_name)}"
        response = requests.post(
            url=url,
            json=data.tasks,
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise WorkflowException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise WorkflowException(
                status_code=response.status_code,
                message=f"Failed to skip steps in workflow {workflow_name}",
                response_data=response.json(),
            )
        return Workflow.parse_obj(response.json())

    def rerun_workflow(
        self, workflow_name: str, data: WorkflowRequest
    ) -> RunWorkflowResponse:
        url = f"{self.configs.base_url}/{self.endpoints.RERUN_WORKFLOW.format(WORKFLOW_NAME=workflow_name)}"
        response = requests.post(
            url=url,
            json=data.dict(),
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise WorkflowException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise WorkflowException(
                status_code=response.status_code,
                message=f"Failed to re-run workflow {workflow_name}",
                response_data=response.json(),
            )
        return RunWorkflowResponse.parse_obj(response.json())

    def run_workflow(
        self, workflow_name: str, data: WorkflowRequest
    ) -> RunWorkflowResponse:
        url = f"{self.configs.base_url}/{self.endpoints.RUN_WORKFLOW.format(WORKFLOW_NAME=workflow_name)}"
        response = requests.post(
            url=url,
            json=data.dict(),
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise WorkflowException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise WorkflowException(
                status_code=response.status_code,
                message=f"Failed to run workflow {workflow_name}",
                response_data=response.json(),
            )
        return RunWorkflowResponse.parse_obj(response.json())

    def get_workflow_status(
        self, show_internal_steps: bool, workflow_id: str, workflow_run_id: str
    ) -> WorkflowStatusResponse:
        url = f"{self.configs.base_url}/{self.endpoints.WORKFLOW_STATUS.format(WORKFLOW_ID=workflow_id,WORKFLOW_RUN_ID=workflow_run_id)}"
        response = requests.get(
            url=url,
            params=[("show_internal_steps", show_internal_steps)],
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise WorkflowException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise WorkflowException(
                status_code=response.status_code,
                message="Failed to get workflows",
                response_data=response.json(),
            )
        return WorkflowStatusResponse.parse_obj(response.json())
