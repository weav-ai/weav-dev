# Document and Workflow Management Scripts

## Overview

This repository contains two Python scripts, `run_workflow.py` and `upload_and_get_document.py`, which are used to upload documents, retrieve documents, and interact with workflows. They allow users to perform tasks such as uploading documents, retrieving pages from documents, and running workflows on uploaded documents.

## Setup 

**Step 1:**
Install requirements

```pip install -r requirements.txt```

**Step 2:**
Add environment variables to the `.env` file

```
ENV = "https://subdomain.weav.ai"
AUTH_TOKEN = "eyJhbGciOiJ..."
```

## Script Descriptions

### 1. `run_workflow.py`

This script provides functionality for uploading and retrieving documents. It interacts with the `DocumentOperations` service and provides three primary actions:

- **Upload a Document (`upload_document`)**: Upload a document to the system, optionally specifying a folder ID.
- **Retrieve a Document (`get_document`)**: Retrieve a document using its unique document ID.
- **Retrieve a Page from a Document (`get_page`)**: Retrieve a specific page from a document using its document ID and page number.

**Functions**:
- `upload_document(file_path: str, folder_id: Optional[str] = "")`: Uploads a document from a given file path.
- `get_document(document_id: str)`: Retrieves a document based on its ID.
- `get_document_by_page(document_id: str, page_number: int)`: Retrieves a specific page from a document.

**Usage**:
Run the script with the appropriate action using command-line arguments:

```bash
python run_workflow.py --action <action>
```

Replace `<action>` with one of the following:

1. upload_document
2. get_document
3. get_page

The script will prompt for additional inputs based on the action chosen, such as file path, document ID, or page number.

### 2. `upload_and_get_document.py`

This script focuses on running workflows on uploaded documents and retrieving workflow statuses. It interacts with the WorkflowService and provides multiple actions:

- **Retrieve All Workflows (`get_all_workflows`)**: List all available workflows.
- **Run a Workflow (`run_workflow`)**: Run a specified workflow on a given document ID.
- **Retrieve Workflow Status (`get_workflow_status`)**: Retrieve the status of a workflow using the workflow ID and run ID.

**Functions**:
- `get_workflow_status(workflow_id: str, workflow_run_id: str)`: Retrieves the status of a specific workflow run.
- `get_all_workflows()`: Retrieves all available workflows.
- `run_workflow(workflow_name: str, document_id: str, data: Optional[Dict[Any, Any]] = None)`: Runs a workflow on a given document.

**Usage**: 
Run the script with the appropriate action using command-line arguments:

```bash
python upload_and_get_document.py --action <action>
```

Replace `<action>` with one of the following:

1. get_all_workflows
2. run_workflow
3. get_workflow_status

The script will prompt for additional inputs based on the action chosen, such as workflow ID, workflow name, document ID, and additional parameters.

Example Commands

#### **Upload a Document**:
```python run_workflow.py --action upload_document```

The script will ask for the file path and an optional folder ID.

#### **Retrieve a Document**:
```python run_workflow.py --action get_document```

The script will ask for the document ID.

#### **Run a Workflow**:
```python upload_and_get_document.py --action run_workflow```

The script will list available workflows, prompt for a workflow name, and ask for the document ID.