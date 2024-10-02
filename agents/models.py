from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class GetAllAgentsResponse(BaseModel):
    response: List[str]


class GetAgentRequest(BaseModel):
    user_input: str
    chat_id: str
    stream: bool
    agent_type: str


class GetAgentResponse(BaseModel):
    id: Optional[str] = None
    event: Optional[str] = None
    data: Optional[str] = None
    retry: Optional[int] = None


class Message(BaseModel):
    message_id: Optional[str]
    chat_id: Optional[str]
    text: Optional[str]
    timestamp: Optional[datetime]
    type: Optional[str]
    vote: Optional[str]
    search_results: Optional[List[str]]
    generate_button: Optional[str] = None
    tags: Optional[List[str]]


class ChatHistoryResponse(BaseModel):
    messages: List[Message]
