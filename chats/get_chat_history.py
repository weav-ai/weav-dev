# python3 chats/get_chat_history.py --chat_id 6298680e-0e05-4d8a-b6d8-c98f213c1c6e

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config_models import LoadConfigurations, ServiceType
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
        help="Skip the first N messages",
    )
    args = parser.parse_args()

    chat_history_response = chat_service.get_chat_history(chat_id=args.chat_id)
    pprint(chat_history_response.dict())
