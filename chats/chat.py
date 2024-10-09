# python3 chats/chat.py --chat_id 66e0fba3089fbd21c4d --user_input "Summarize this doc?" --file_id 66e0fba3089fbd21c4dd80c3

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models import ChatRequest
from config_models import LoadConfigurations, ServiceType, get_bool_value, BOOL_CHOICES
from service import ChatService
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.CHATS)
    chat_service = ChatService(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--chat_id",
        type=str,
        required=True,
        help="The ID of the chat",
    )

    parser.add_argument(
        "--file_id",
        type=str,
        required=True,
        help="File ID",
    )

    parser.add_argument(
        "--user_input",
        type=str,
        required=True,
        help="The User request",
    )

    args = parser.parse_args()

    body = ChatRequest(
        user_input=args.user_input,
        file_id=args.file_id,
        chat_id=args.chat_id,
        stream=False,
    )

    chat_response = chat_service.chat(chat_request=body)
    pprint(chat_response.model_dump())
