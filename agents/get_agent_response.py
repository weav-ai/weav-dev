# python3 agents/get_agent_response.py --user_input "Summarize the document" --chat_id "google-oauth2|117349365869611297391_Insurance Underwriting AI Agent" --agent_id "<agent_id>"
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from service import AgentOperations
from config_models import LoadConfigurations, ServiceType, BOOL_CHOICES, get_bool_value
import argparse


if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.AGENT)
    agent_service = AgentOperations(configs=configs)

    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument("--user_input", type=str, required=True, help="User input text")
    parser.add_argument("--chat_id", type=str, required=True, help="Chat ID")

    parser.add_argument("--agent_id", type=str, required=True, help="Agent ID")

    args = parser.parse_args()

    agent_response = agent_service.get_agent_response(
        user_input=args.user_input, chat_id=args.chat_id, agent_id=args.agent_id
    )
    print(agent_response)
