# python3 documents/forms/filter_form_instances.py --scope "all_documents" --category "Test" --query "" --form_id 66e9e1ad47fff0950cba17ea --doc_id 66df87ec2b1edfc0dc3b556f --status DONE

import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from config_models import LoadConfigurations, ServiceType, BOOL_CHOICES, get_bool_value
from documents.service import FormOperations
from documents.models import FilterFormInstanceRequest

if __name__ == "__main__":
    configs = LoadConfigurations().set_config(service=ServiceType.DOCUMENT)
    form_operation = FormOperations(configs=configs)
    parser = argparse.ArgumentParser(description="Provide parameters for the script.")

    parser.add_argument(
        "--scope",
        type=str,
        required=True,
        help="Scope to search form instances",
        choices=[
            "all_documents",
            "current_document",
            "my_documents",
            "shared_documents",
        ],
    )
    parser.add_argument(
        "--status",
        type=str,
        default="",
        required=False,
        choices=["NOT_STARTED", "IN_PROGRESS", "DONE", "FAILED"],
        help="Document status to be matched",
    )
    parser.add_argument(
        "--category",
        type=str,
        default="",
        required=False,
        help="Document category to be matched",
    )
    parser.add_argument(
        "--query",
        type=str,
        default="",
        required=False,
        help="This string is matched in category and description",
    )
    parser.add_argument(
        "--form_id",
        type=str,
        default="",
        required=False,
        help="Unique identifier for the form",
    )
    parser.add_argument(
        "--doc_id",
        type=str,
        default="",
        required=False,
        help="Unique identifier for the document",
    )
    parser.add_argument(
        "--only_latest",
        type=bool,
        choices=BOOL_CHOICES,
        default="True",
        required=False,
        help="Only latest form extraction",
    )
    parser.add_argument(
        "--skip",
        type=int,
        default=0,
        required=False,
        help="Number of documents to skip",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        required=False,
        help="Max fetch size",
    )

    parser.add_argument(
        "--all",
        type=str,
        choices=BOOL_CHOICES,
        default="False",
        required=False,
        help="If set to true, all instances are fetched",
    )
    args = parser.parse_args()

    body = FilterFormInstanceRequest(
        scope=args.scope,
        status=args.status,
        category=args.category,
        query=args.query,
        form_id=args.form_id,
        doc_id=args.doc_id,
        only_latest=get_bool_value(args.only_latest),
        skip=args.skip,
        limit=args.limit,
        all=get_bool_value(args.all),
    )
    form_create_response = form_operation.filter_form_instances(form_data=body)
    print(form_create_response.model_dump())
