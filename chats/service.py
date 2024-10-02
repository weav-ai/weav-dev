from config_models import ConfigModel, ServiceEndpoints, AUTHENTICATION_FAILED_MESSAGE
from chats.models import (
    GetChatLogsRequest,
    ChatLogsResponse,
    ChatHistoryResponse,
    ChatResponse,
)
from models import ChatRequest

from exceptions import ChatServiceException
import requests


class ChatService:
    def __init__(self, configs: ConfigModel):
        self.configs = configs
        self.endpoints = ServiceEndpoints()

    def get_chat_logs(self, chat_logs_request: GetChatLogsRequest) -> ChatLogsResponse:
        url = f"{self.configs.base_url}/{self.endpoints.CHAT_LOGS}"
        params = [
            ("skip", chat_logs_request.skip),
            ("limit", chat_logs_request.limit),
            ("start_datetime", chat_logs_request.start_datetime),
            ("end_datetime", chat_logs_request.end_datetime),
            ("is_sop_chat", chat_logs_request.is_sop_chat),
        ]
        filtered_params = [(k, v) for k, v in params if v is not None and v != ""]

        response = requests.get(
            url=url,
            params=filtered_params,
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise ChatServiceException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise ChatServiceException(
                status_code=response.status_code,
                message="Failed to retrieve chat logs",
                response_data=response.json(),
            )
        return ChatLogsResponse(**response.json())

    def get_chat_history(self, chat_id: str) -> ChatHistoryResponse:
        url = f"{self.configs.base_url}/{self.endpoints.CHAT_HISTORY}"
        params = [("chat_id", chat_id)]

        response = requests.get(
            url=url,
            params=params,
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise ChatServiceException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise ChatServiceException(
                status_code=response.status_code,
                message="Failed to retrieve chat logs",
                response_data=response.json(),
            )
        return ChatHistoryResponse(**response.json())

    def chat(self, chat_request: ChatRequest) -> ChatResponse:
        url = f"{self.configs.base_url}/{self.endpoints.CHAT}"
        response = requests.post(
            url=url,
            json=chat_request.dict(),
            headers={"Authorization": f"Bearer {self.configs.auth_token}"},
        )
        if response.status_code == 401:
            raise ChatServiceException(
                status_code=response.status_code,
                message=AUTHENTICATION_FAILED_MESSAGE,
                response_data=response.json(),
            )
        elif response.status_code != 200:
            raise ChatServiceException(
                status_code=response.status_code,
                message="Failed to send chat",
                response_data=response.json(),
            )
        return ChatResponse(**response.json())
