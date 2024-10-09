import sys
import os
import argparse
from typing import Optional

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config_models import LoadConfigurations, ServiceType

from documents.service import DocumentOperations


document_configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)

document_operation = DocumentOperations(configs=document_configs)


def upload_document(file_path: str, folder_id: Optional[str] = ""):
    print(f"Uploading document {file_path.split('/')[-1]}")

    document_create_response = document_operation.create_document(
        file_path=file_path, folder_id=folder_id
    )

    print("Uploaded document!")

    document_id = document_create_response.id
    print(f"Document ID: {document_id}")

    return document_create_response.model_dump()


def get_document(document_id: str):
    get_document_response = document_operation.get_document(document_id=document_id)

    print("Fetched document")

    return get_document_response.model_dump()


def get_document_by_page(document_id: str, page_number: int):
    get_document_response = document_operation.get_page(
        document_id=document_id, page_number=page_number
    )

    print(f"Fetched page number {page_number}")

    return get_document_response.model_dump()


def main():
    print("Script to Upload and Retrieve Documents")
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--action",
        type=str,
        choices=["upload_document", "get_document", "get_page"],
        help="Choose whether to upload or get a document",
    )

    args = parser.parse_args()

    if args.action is None or args.action not in [
        "get_document",
        "get_page",
        "upload_document",
    ]:
        print(
            "No action specified. Please enter 'get_document', 'get_page' or 'upload_document'."
        )
        parser.print_usage()
        return

    if args.action == "upload_document":
        file_path = input("Enter file path: ")
        folder_id = input("Enter folder ID: Click enter to skip. ")
        print("Action selected: Upload document")
        response = upload_document(file_path=file_path, folder_id=folder_id)
    elif args.action == "get_document":
        print("Action selected: Retrieve document")
        document_id = input("Enter document ID: ")
        response = get_document(document_id=document_id)
    elif args.action == "get_page":
        print("Action selected: Retrieve page of document")
        document_id = input("Enter document ID: ")
        page_number = input("Enter page number: ")
        response = get_document_by_page(
            document_id=document_id, page_number=int(page_number)
        )

    print(response)


if __name__ == "__main__":
    main()
