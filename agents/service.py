import contextlib
from config_models import ConfigModel, ServiceEndpoints, AUTHENTICATION_FAILED_MESSAGE
from models import (
    GetAllAgentsResponse,
    GetAgentRequest,
    ChatHistoryResponse,
    GetAgentResponse,
)
from exceptions import AgentServiceException
import requests
from pydantic import ValidationError
from typing import List


class AgentService:
    def __init__(self, configs: ConfigModel):
        self.configs = configs
        self.endpoints = ServiceEndpoints()

    def get_agent_types(self) -> GetAllAgentsResponse:
        url = f"{self.configs.base_url}/{self.endpoints.GET_AGENT_TYPES}"
        response = requests.get(
            url=url, headers={"Authorization": f"Bearer {self.configs.auth_token}"}
        )
        if response.status_code == 401:
            raise AgentServiceException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise AgentServiceException(
                status_code=response.status_code,
                message="Failed to get agent types",
                response_data=response.json(),
            )
        return GetAllAgentsResponse(response=response.json())

    def get_agent_response(
        self, get_agent_request_body: GetAgentRequest
    ) -> List[GetAgentResponse]:
        url = f"{self.configs.base_url}/{self.endpoints.GET_AGENT_RESPONSE}"
        response = requests.post(
            url=url,
            json=get_agent_request_body.dict(),
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise AgentServiceException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code == 422:
            raise AgentServiceException(
                status_code=response.status_code,
                message="Validation failed, ensure data entered is correct",
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise AgentServiceException(
                status_code=response.status_code,
                message="Failed to get agent types",
                response_data=response.json(),
            )

        def parse_sse_event(event_string: str) -> GetAgentResponse:
            lines = event_string.splitlines()
            event_data = {}

            for line in lines:
                if line.startswith("data:"):
                    event_data["data"] = line[len("data: ") :].strip()
                elif line.startswith("id:"):
                    event_data["id"] = line[len("id: ") :].strip()
                elif line.startswith("event:"):
                    event_data["event"] = line[len("event: ") :].strip()
                elif line.startswith("retry:"):
                    event_data["retry"] = int(line[len("retry: ") :].strip())

            with contextlib.suppress(ValidationError):
                return GetAgentResponse(**event_data)

        resp = []
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                event = parse_sse_event(decoded_line)
                resp.append(event)
        return resp

    def get_chat_history(self, chat_id: str) -> ChatHistoryResponse:
        url = f"{self.configs.base_url}/{self.endpoints.GET_CHAT_HISTORY.format(CHAT_ID=chat_id)}"
        response = requests.get(
            url=url,
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise AgentServiceException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise AgentServiceException(
                status_code=response.status_code,
                message="Failed to get chat history",
                response_data=response.json(),
            )
        return ChatHistoryResponse(**response.json())

    def delete_chat_history(self, chat_id: str) -> str:
        url = f"{self.configs.base_url}/{self.endpoints.DELETE_CHAT_HISTORY}"
        response = requests.delete(
            url=url,
            json={"chat_id": chat_id},
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise AgentServiceException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code == 422:
            raise AgentServiceException(
                status_code=response.status_code,
                message="Validation failed, ensure data entered is correct",
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise AgentServiceException(
                status_code=response.status_code,
                message="Failed to get chat history",
                response_data=response.json(),
            )
        return "Success"
