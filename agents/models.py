from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


class GetAllAgentsResponse(BaseModel):
    response: List[str]


class GetAgentRequest(BaseModel):
    user_input: str
    chat_id: str
    stream: bool
    agent_id: str


class GetAgentResponse(BaseModel):
    id: Optional[str] = ""
    event: Optional[str] = ""
    data: Optional[str] = ""
    retry: Optional[int] = None


class Message(BaseModel):
    message_id: Optional[str] = ""
    chat_id: Optional[str] = ""
    text: Optional[str] = ""
    timestamp: Optional[datetime] = None
    type: Optional[str] = ""
    vote: Optional[str] = ""
    search_results: Optional[List[str]] = []
    generate_button: Optional[str] = ""
    tags: Optional[List[str]] = []


class ChatHistoryResponse(BaseModel):
    messages: List[Message]


class Intent(BaseModel):
    index: int
    name: str
    description: str
    event_message: str
    allowed_actions: List[str]


class Intents(BaseModel):
    event_message: str
    intents: List[Intent]


class Action(BaseModel):
    name: str
    description: str
    event_message: str
    input_schema: str
    identifier: str
    llm_model_name: Optional[str] = None
    type: str
    folder_name_keywords: List[str] = Field(default_factory=list)
    folder_ids: List[str] = Field(default_factory=list)
    enable_context_relevancy_filtering: bool = False
    k: Optional[int] = None
    domain: Optional[str] = None
    exclude_sites: List[str] = Field(default_factory=list)
    documents: Dict[str, Any] = Field(default_factory=dict)
    tmp_image_path: Optional[str] = None
    url: Optional[str] = None
    rest_verb: Optional[str] = None
    max_char: Optional[int] = None
    folder_id: Optional[str] = None


class PublishResultsAction(BaseModel):
    name: str
    description: str
    event_message: str
    input_schema: str
    identifier: str
    llm_model_name: Optional[str] = None
    type: str
    folder_name_keywords: List[str] = Field(default_factory=list)
    folder_id: str = ""


class PublishResultsConfiguration(BaseModel):
    publish_only_if_asked: bool = False
    publish_action: PublishResultsAction


class AgentConfiguration(BaseModel):
    id: str
    name: str
    verbose: bool = False
    tone: str = "professional"
    background: str = ""
    custom_instructions: str = ""
    reply_format: str
    max_iterations: int = 5
    llm_model_name: Optional[str] = ""
    intents: Intents
    actions: List[Action]
    publish_results_configuration: PublishResultsConfiguration


class AgentConfigurations(BaseModel):
    configurations: Optional[List[AgentConfiguration]] = []
