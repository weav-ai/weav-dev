# python3 documents/folders/get_writable_folders.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType
from documents.service import FolderOperations
from pprint import pprint

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    folder_operation = FolderOperations(configs=configs)

    folder_create_response = folder_operation.get_writable_folders()
    pprint(folder_create_response.model_dump())
