# python3 agents/delete_chat_history.py --chat_id "google-oauth2|117349365869611297391_Insurance Underwriting AI Agent"

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config_models import LoadConfigurations, ServiceType
from service import AgentService


if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.AGENT)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument("--chat_id", type=str, required=True, help="Chat ID.")

    args = parser.parse_args()
    print("You are about to perform a DELETE operation.")
    confirm = str(input("Are you sure you want to continue? (Y/N): "))
    if confirm.lower() in {"yes", "y"}:
        agent_service = AgentService(configs=configs)
        agent_types = agent_service.delete_chat_history(chat_id=args.chat_id)
        print(agent_types)
    else:
        print("Cancelled operation.")
