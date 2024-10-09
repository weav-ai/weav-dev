# python3 documents/documents/get_document_tags.py

import sys
import os
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType
from documents.service import DocumentOperations

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    document_operation = DocumentOperations(configs=configs)

    get_tags_response = document_operation.get_document_tags()
    pprint(get_tags_response.model_dump())
