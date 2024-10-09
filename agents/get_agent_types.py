# python3 agents/get_agent_types.py

import sys
import os
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config_models import LoadConfigurations, ServiceType
from service import AgentService


if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.AGENT)
    agent_service = AgentService(configs=configs)
    agent_types = agent_service.get_agent_types()

    pprint(agent_types.response)
