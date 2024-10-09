# python3 agents/get_chat_history.py --chat_id "google-oauth2|117349365869611297391_Insurance Underwriting AI Agent"

import sys
import os
import argparse
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config_models import LoadConfigurations, ServiceType
from service import AgentService


if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.AGENT)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument("--chat_id", type=str, required=True, help="Chat ID")

    args = parser.parse_args()
    agent_service = AgentService(configs=configs)
    agent_types = agent_service.get_chat_history(chat_id=args.chat_id)
    pprint(dict(agent_types))
