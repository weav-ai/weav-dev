import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from chats.models import GetChatLogsRequest
from config_models import LoadConfigurations, ServiceType
from service import ChatService
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.CHATS)
    chat_service = ChatService(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--skip",
        type=int,
        default=0,
        required=False,
        help="Skip the first N messages",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        required=False,
        help="Choose how many chats to retrieve",
    )

    parser.add_argument(
        "--start_datetime",
        type=str,
        default=None,
        required=False,
        help="Date after which chats are to be retrieved",
    )

    parser.add_argument(
        "--end_datetime",
        type=str,
        default=None,
        required=False,
        help="Date before which chats are to be retrieved",
    )

    args = parser.parse_args()
    chat_logs_request = GetChatLogsRequest(
        skip=args.skip,
        limit=args.limit,
        start_datetime=args.start_datetime,
        end_datetime=args.end_datetime,
        is_sop_chat=False,
    )

    chat_log_response = chat_service.get_chat_logs(chat_logs_request=chat_logs_request)
    pprint(chat_log_response.model_dump())
