# python3 workflows/get_workflow_status.py --workflow_id process_form_workflow --workflow_run_id 66df87ec2b1edfc0dc3b556f_f6328cd2-fbbf-41d0-a756-b111041cae6c

from config_models import ConfigModel, ServiceEndpoints, AUTHENTICATION_FAILED_MESSAGE
from workflows.models import (
    GetAllWorkflowsResponse,
    Workflow,
    SkipStepsInWorkflowRequest,
    RunWorkflowResponse,
    WorkflowRequest,
    WorkflowStatusResponse,
    DocumentWorkflowRunsResponse,
)
from workflows.exceptions import WorkflowException
import requests
from typing import Optional


class WorkflowService:
    def __init__(self, configs: ConfigModel):
        self.configs = configs
        self.endpoints = ServiceEndpoints()

    def get_all_workflows(
        self, show_internal_steps: bool = False
    ) -> GetAllWorkflowsResponse:
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

        return Workflow.model_validate(response.json())

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
        return Workflow.model_validate(response.json())

    def rerun_workflow(
        self, workflow_name: str, data: WorkflowRequest
    ) -> RunWorkflowResponse:
        url = f"{self.configs.base_url}/{self.endpoints.RERUN_WORKFLOW.format(WORKFLOW_NAME=workflow_name)}"
        response = requests.post(
            url=url,
            json=data.model_dump(),
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
        return RunWorkflowResponse.model_validate(response.json())

    def run_workflow(
        self, workflow_name: str, data: WorkflowRequest
    ) -> RunWorkflowResponse:
        url = f"{self.configs.base_url}/{self.endpoints.RUN_WORKFLOW.format(WORKFLOW_NAME=workflow_name)}"
        response = requests.post(
            url=url,
            json=data.model_dump(),
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
        return RunWorkflowResponse.model_validate(response.json())

    def get_workflow_status(
        self,
        workflow_id: str,
        workflow_run_id: str,
        show_internal_steps: Optional[bool] = False,
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
        return WorkflowStatusResponse.model_validate(response.json())

    def get_workflow_runs_for_document(
        self,
        doc_id: str,
        state: str = "",
        query: str = "",
        skip: int = 0,
        limit: int = 25,
    ) -> DocumentWorkflowRunsResponse:
        params = [
            ("doc_id", doc_id),
            ("state", state),
            ("query", query),
            ("skip", skip),
            ("limit", limit),
        ]
        filtered_params = [
            (name, value) for name, value in params if value not in ("", None)
        ]
        url = f"{self.configs.base_url}/{self.endpoints.WORKFLOW_RUNS}"
        response = requests.get(
            url=url,
            params=filtered_params,
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
                message=f"Failed to get workflow runs for {doc_id}",
                response_data=response.json(),
            )
        return DocumentWorkflowRunsResponse.model_validate(response.json())
