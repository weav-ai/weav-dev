from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime


class GetChatLogsRequest(BaseModel):
    skip: int = 0
    limit: int = 25
    start_datetime: Optional[str]
    end_datetime: Optional[str]
    is_sop_chat: bool


class Message(BaseModel):
    id: str
    timestamp: datetime
    type: str
    valid: Optional[bool]
    vote: str
    chat_id: str
    user_id: str
    tags: Optional[List[str]]
    text: str


class ChatLogsResponse(BaseModel):
    messages: Optional[List[Message]]
    total_records: int
    current_skip: int


class ChatHistoryMessage(BaseModel):
    message_id: str
    chat_id: str
    text: str
    timestamp: str
    type: str
    vote: str
    search_results: List[Any]
    generate_button: Optional[bool]
    tags: List[Any]


class ChatHistoryResponse(BaseModel):
    messages: List[ChatHistoryMessage]


class ChatRequest(BaseModel):
    user_input: str
    file_id: str
    chat_id: str
    stream: bool


class Classification(BaseModel):
    page_class: Optional[str]
    page_sections: Optional[List[str]]
    page_no: Optional[int]


class SearchResult(BaseModel):
    text: str
    file_id: str
    page_number: int
    score: float
    rank: int
    file_name: str
    classification: Optional[Classification]
    section_headers: Optional[List[str]]
    tags: Optional[List[str]]


class ChatResponse(BaseModel):
    message_id: str
    chat_id: str
    text: str
    timestamp: datetime
    type: str
    vote: str
    search_results: List[SearchResult]
    generate_button: Optional[str]
    tags: List[str]
