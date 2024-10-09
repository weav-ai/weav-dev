## Process document tutorial

## Setup

Pull the GitHub code

```bash
git clone https://github.com/weav-ai/weav-dev.git
```

Install requirements

```bash
	pip3 install -r requirements.txt
```

Add variables to `.env` file

```bash
ENV = "https://<env_name>"
AUTH_TOKEN = "eyJhbGci...."

```

For example

```bash
ENV = "https://subdomain.weav.ai"
AUTH_TOKEN = "eyJhbGciOiJ..."
```

---

---

## Agents

### Get Agent Types

Fetches all the agents present on the platform.

```bash
python3 agents/get_agent_types.py
```

**Response:**

```bash
['Agent A', 'Agent B' ..... ,'Agent C']
```

### Get Agent Response

Fetches the response of a selected agent from the platform based on user input.

```bash
python3 agents/get_agent_response.py --user_input "Summarize the document" --chat_id "google-oauth2|117349365869611297391_Insurance Underwriting AI Agent" --agent_type "Insurance Underwriting AI Agent"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| user_input | The question provided to the agent | Required |
| agent_type | The Agent type to be used | Required |
| chat_id | Chat ID in which the conversation takes place | Required |

**Response:**

```bash
[GetAgentResponse(id=None, event=None, data='{"type": "assistant", "chat_id": "google-oauth2|117349365869611297391_Insurance Underwriting AI Agent", "vote": "no vote", "message_id": "d79c34f5-f4f3-4170-8baa-8baf2efea2a4", "search_results": [], "generate_button": null, "tags": [], "text": "**Analyzing request...<br><br>** ", "timestamp": "2024-09-25 19:12:20.178930+00:00"}', retry=None),...]
```

---

### Get Chat History

Get all chat history with selected agent.

```bash
python3 agents/get_chat_history.py --chat_id "google-oauth2|117349365869611297391_Insurance Underwriting AI Agent"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| chat_id | Chat ID in which the conversation takes place | Required |

**Response:**

```bash
{'messages': [Message(message_id='423a02c6-ad21-4438-b3cc-9be2ffa65197', chat_id='google-oauth2|117349365869611297391_Insurance Underwriting AI Agent', text='whatsup', timestamp=datetime.datetime(2024, 9, 24, 1, 5, 29, 775000), type='user', vote='no vote', search_results=[], generate_button=None, tags=[]), Message(message_id='f79bf3f7-3a52-47f8-8bf8-7e792c729b20', chat_id='google-oauth2|117349365869611297391_Insurance Underwriting AI Agent', text="Hello! How can I assist you today with your insurance underwriting needs? If you have any specific questions or requests, please let me know, and I'll be happy to help.<br><br>\n", timestamp=datetime.datetime(2024, 9, 24, 1, 5, 36, 20000), type='assistant', vote='no vote', search_results=[], generate_button=None, tags=[])..]}
```

---

### Delete Chat History

Get all chat history with selected agent. The user is prompted to confirm their choice and must respond with either “Y” or “N”.

```bash
python3 agents/get_chat_history.py --chat_id "google-oauth2|117349365869611297391_Insurance Underwriting AI Agent"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| chat_id | Chat ID in which the conversation takes place | Required |

**Response:**

```bash
Success
```

---

---

## Workflows

### Get all workflows

Get a list of all workflows that are present on the [Weav.ai](http://Weav.ai) platform.

```bash
 python3 workflows/get_all_workflows.py --show_internal_steps false
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| show_internal_steps | Set to true to show detailed internal steps of the workflowx | Optional (default : False) | false, f, False, true, t, True |

**Response:**

```bash
{
   "workflows":[
      {
         "name":"dagtasktest",
         "params":[
            
         ],
         "tasks":[
            {
               "downstream_tasks":[
                  
               ],
               "is_active":true,
               "name":"only_if_failed"
            },
            {
               "downstream_tasks":[
                  
               ],
               "is_active":true,
               "name":"only_if_success"
            }
         ]
      }
   ]
}
```

---

### Get Single workflow

Get all the steps that are present inside a particular workflow. 

```bash
python3 workflows/get_single_workflow.py --workflow_name dagtasktest --show_internal_steps false
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| show_internal_steps | Set to true to show detailed internal steps | Optional (default : False) | false, f, False, true, t, True |
| workflow_name | The name of the workflow to be fetched | Required | String |

**Response:**

```bash
{
   "name":"dagtasktest",
   "params":[
      
   ],
   "tasks":[
      {
         "downstream_tasks":[
            
         ],
         "is_active":true,
         "name":"only_if_failed"
      },
      {
         "downstream_tasks":[
            
         ],
         "is_active":true,
         "name":"only_if_success"
      },
      {
         "downstream_tasks":[
            "second"
         ],
         "is_active":true,
         "name":"first"
      },
      {
         "downstream_tasks":[
            "third"
         ],
         "is_active":true,
         "name":"second"
      },
      {
         "downstream_tasks":[
            "only_if_success",
            "only_if_failed"
         ],
         "is_active":true,
         "name":"third"
      },
      {
         "downstream_tasks":[
            "second",
            "third",
            "first"
         ],
         "is_active":true,
         "name":"split"
      }
   ]
}
```

---

### Run Workflow

Run a particular workflow for a document. The name of the workflow can be obtained from `name` field in the `Get all workflows` API response demonstrated above.

```bash
python3 workflows/run_workflow.py --doc_id 66e0fba3089fbd21c4dd80c3 --workflow_name dagtest --data "{\"form_id\":\"66fe5c58b1d0dfb13c9975f3\"}"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| workflow_name | Name of the workflow to be run | Required |  |
| doc_id | Document for which the workflow has to be run | Required |  |
| data | Any extra parameters that are required by the worflow | Optional | Stringified JSON |

**Response:**

```bash
{
   "created_at":"2024-09-25T19:33:32.000000+00:00",
   "document_id":"66e0fba3089fbd21c4dd80c3",
   "document_name":"AAPL_10Q.pdf",
   "end_date":"None",
   "in_folders":[
      "66e0f93093798ee1c937e39a"
   ],
   "run_id":"66e0fba3089fbd21c4dd80c3_3df1b127-9ea5-4714-9bf5-b1a5653859f6",
   "start_date":"None",
   "state":"None",
   "workflow_id":"dagtest"
}
```

---

### Get Workflow status

Upon running a workflow, check the status of the run.

```bash
python3 workflows/get_workflow_status.py --workflow_id "dagtasktest" --workflow_run_id "66e0fba3089fbd21c4dd80c3_3df1b127-9ea5-4714-9bf5-b1a5653859f6"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| show_internal_steps | Set to true to show detailed internal steps | Optional (default : False) | false, f, False, true, t, True |
| workflow_id | Document identifier for which the workflow has to be run | Required |  |
| workflow_run_id | The run ID of the workflow | Required |  |

<aside>
💡

The `workflow_run_id` and `workflow_id` can be obtained from the `run_id` and `workflow_id` fields in the `Run Workflow` response above.

</aside>

**Response:**

```bash
{
    "document_id": "66fe1752927ce8c0ebda42b9",
    "end_date": datetime.datetime(2024, 10, 3, 4, 23, 42, 58430, tzinfo=TzInfo(UTC)),
    "start_date": datetime.datetime(2024, 10, 3, 4, 14, 45, 30553, tzinfo=TzInfo(UTC)),
    "status": "failed",
    "tasks": [
        {
            "end_date": datetime.datetime(
                2024, 10, 3, 4, 20, 4, 293969, tzinfo=TzInfo(UTC)
            ),
            "failed_task_ids": [-1],
            "name": "set_processing_to_in_state__1",
            "start_date": datetime.datetime(
                2024, 10, 3, 4, 20, 4, 293969, tzinfo=TzInfo(UTC)
            ),
            "status": "failed",
            "task_status_summary": {
                "failed": 1,
                "queued": 0,
                "running": 0,
                "skipped": 0,
                "success": 0,
            },
        },
       .
       .
       .
    ],
}
```

---

### Rerun workflow

If a workflow has already run before, re-run the workflow as per requirements

```bash
python3 workflows/rerun_workflow.py --doc_id 66df87ec2b1edfc0dc3b556f --workflow_name "dagtest"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| workflow_name | Name of the workflow to be run | Required |  |
| doc_id | Document for which the workflow has to be run | Required |  |
| data | Any extra parameters that are required by the worflow | Optional | Stringified JSON |

**Response:**

```bash
{
   "created_at":"2024-09-25T19:33:32.000000+00:00",
   "document_id":"66df87ec2b1edfc0dc3b556f",
   "document_name":"AAPL_10Q.pdf",
   "end_date":"None",
   "in_folders":[
      "66e0f93093798ee1c937e39a"
   ],
   "run_id":"66e0fba3089fbd21c4dd80c3_3df1b127-9ea5-4714-9bf5-b1a5653859f6",
   "start_date":"None",
   "state":"None",
   "workflow_id":"dagtest"
}
```

---

### Skip steps in a workflow

Allow the workflow to skip any steps that are present in the workflow.

```bash
python3 workflows/skip_tasks.py --workflow_name "dagtest" --tasks task_1 task_2
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| workflow_name | Name of the workflow to be run | Required |  |
| tasks | A list of tasks to be skipped | Required | Strings seperated by spaces (Example —tasks task_1 task_2 |

---

### Get Workflow Runs For Document

Fetches all the workflows runs for a particular document.

```bash
python3 workflows/get_workflows_for_document.py --doc_id 66df87ec2b1edfc0dc3b556f --state "success" --query "ANNUAL REPORT" --skip 0 --limit 1
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| doc_id | Document for which the workflow has to be fetched | Required |
| state | State of workflow | Optional |
| query | This string is matched with workflow and document name | Optional |
| skip | Number of workflows to skip | Optional |
| limit | Max fetch size | Optional |

**Response:**

```bash
{
   "docs":[
      {
         "created_at":"None",
         "document_id":"66fe1752927ce8c0ebda42b9",
         "document_name":"66fe1752927ce8c0ebda42b9",
         "end_date":"2024-10-03T20:37:32.405064+00:00",
         "in_folders":[
            
         ],
         "run_id":"66fe1752927ce8c0ebda42b9_078c1e26-a82b-4ada-ac5e-357eac3eb2b3",
         "start_date":"2024-10-03T20:37:26.234912+00:00",
         "state":"failed",
         "workflow_id":"process_form_workflow"
      },
      .
      .
      .
      .
      {
         "created_at":"None",
         "document_id":"66fe1752927ce8c0ebda42b9",
         "document_name":"MCS-CS-Handbook-2022-2023Publish.pdf",
         "end_date":"2024-10-03T04:26:21.715502+00:00",
         "in_folders":[
            
         ],
         "run_id":"66fe1752927ce8c0ebda42b9_2451533e-bbec-4e1a-acd5-0ab686f6d430",
         "start_date":"2024-10-03T04:14:47.246008+00:00",
         "state":"failed",
         "workflow_id":"process_form_workflow"
      }
   ],
   "total":7
}
```

---

---

## Forms

### Create form

Creating a form definition. A form definition is required before running `process_form` workflow.

```bash
python3 documents/forms/create_form.py --name "new form" --category "new" --description "test" --is_shared true --is_searchable true --fields "[{\n  \"name\": \"MICROSOFT FORM\",\n  \"description\": \"A form for microsoft\",\n  \"category\": \"ANNUAL REPORT\",\n  \"fields\": [\n    {\n      \"name\": \"Cost of revenue\",\n      \"field_type\": \"Number\",\n      \"is_array\": false,\n      \"fill_by_search\": false,\n      \"description\": \"Extract cost of revenue\"\n    }\n  ],\n  \"is_searchable\": false,\n  \"is_shared\": false\n}]"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| name | The form name | Required |  |
| category | A category name for the form | Required |  |
| description | The description of the form | Required |  |
| is_shared | A flag to decide sharing permissions | Optional (default : False) | false, f, False, true, t, True |
| is_searchable | A flag to decide visibility | Optional (default : False) | false, f, False, true, t, True |
| fields | Form fields | Optional | Stringified JSON |

Format for `fields`

```bash
[{
  "name": "str",
  "description": "str",
  "category": "str",
  "fields": [
    {
      "name": "str",
      "field_type": "Number",
      "is_array": boolean,
      "fill_by_search": boolean,
      "description": "str"
    }
  ],
  "is_searchable": boolean,
  "is_shared": boolean
}]

## Example stringified version for CLI

"[{\n  \"name\": \"MICROSOFT FORM\",\n  \"description\": \"A form for microsoft\",\n  \"category\": \"ANNUAL REPORT\",\n  \"fields\": [\n    {\n      \"name\": \"Cost of revenue\",\n      \"field_type\": \"Number\",\n      \"is_array\": false,\n      \"fill_by_search\": false,\n      \"description\": \"Extract cost of revenue\"\n    }\n  ],\n  \"is_searchable\": false,\n  \"is_shared\": false\n}]"
```

| **Key** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| name | Name of the Entity | Required |  |
| field_type | The data type of the entity | Required | "Number", "Date", "Text", "Table” |
| description | A short instruction to the prompt about the field | Optional |  |
| is_array | If it’s an entity with multiple values | Optional (default: False) | True, False |
| fill_by_search | Use internet search to fill this information | Optional (default: False | True, False |

**Response:**

```bash
{
   "category":"new",
   "created_at":datetime.datetime(2024, 9, 25, 20, 12, 11, tzinfo=datetime.timezone.utc),
   "description":"True",
   "fields":[
      {
         "description":"Net Sales for the quarter",
         "field_type":"Number",
         "fill_by_search":false,
         "is_array":true,
         "name":"Net Sales"
      }
   ],
   "id":"66f46e9b70dd6d497d9b8a37",
   "is_searchable":true,
   "is_shared":true,
   "name":"new form",
   "user_id":"google-oauth2|117349365869611297391"
}
```

---

### Delete Form definition

Deleting a form definition. The user is prompted to reconfirm the deletion. 

```bash
python3 documents/forms/delete_form_definition.py --form_id 66ea66d547fff0950cba17e
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| form_id | The unique identifier of the form | Required |

**Response:**

```bash
{
   "category":"new",
   "created_at":datetime.datetime(2024, 9, 25, 20, 12, 11, tzinfo=datetime.timezone.utc),
   "description":"True",
   "fields":[
      {
         "description":"Net Sales for the quarter",
         "field_type":"Number",
         "fill_by_search":false,
         "is_array":true,
         "name":"Net Sales"
      }
   ],
   "id":"66f46e9b70dd6d497d9b8a37",
   "is_searchable":true,
   "is_shared":true,
   "name":"new form",
   "user_id":"google-oauth2|117349365869611297391"
}
```

---

### Filter form

Search capabilities to retrieve form definitions

```bash
python3 documents/forms/filter_form.py --query "SECURITIES AND EXCHANGE COMMISSION" --scope "all_forms"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| scope | The scope of search | Required | all_forms, my_forms |
| is_searchable | Filter for visibility | Optional (default : False) | false, f, False, true, t, True |
| query | When applied, string matches category | Optional (default : “”) |  |

**Response:**

```bash
{
   "forms":[
      {
         "category":"SECURITIES AND EXCHANGE COMMISSION",
         "created_at":"2024-09-25T09:13:50Z",
         "description":"",
         "fields":[
            {
               "description":"",
               "field_type":"Date",
               "fill_by_search":false,
               "is_array":false,
               "name":"testEnitity1"
            }
         ],
         "id":"66f3d44eeb87303bc52bb9b4",
         "is_searchable":false,
         "is_shared":false,
         "name":"test",
         "user_id":"google-oauth2|117349365869611297391"
      }
   ]
}
```

---

### Get form definitions

Fetching the form definition of a particular form.

```bash
python3 documents/forms/get_form_definition.py --form_id "66f46e9b70dd6d497d9b8a37
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| form_id | Form ID | Required |

**Response:**

```bash
{
   "category":"SECURITIES AND EXCHANGE COMMISSION",
   "created_at":"2024-09-25T09:13:50Z",
   "description":"",
   "fields":[
      {
         "description":"",
         "field_type":"Date",
         "fill_by_search":false,
         "is_array":false,
         "name":"testEnitity1"
      }
   ],
   "id":"66f3d44eeb87303bc52bb9b4",
   "is_searchable":false,
   "is_shared":false,
   "name":"test",
   "user_id":"google-oauth2|117349365869611297391"
}
```

---

### Update form definition

Updating the definition of a form such as name, description, entities and their data etc.

```bash
python3 documents/forms/update_form_definition.py --form_id 66f46e9b70dd6d497d9b8a37 --name "update" --category "new" --description "Test desc" --is_shared false --is_searchable false
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| form_id | Form identifier | Required |  |
| name | Form name | Required |  |
| category | Form category | Required |  |
| description  | Form description | Optional (default : “”) |  |
| is_shared | Filter for sharing permissions | Optional (default : False) | false, f, False, true, t, True |
| is_searchable | Filter for visibility | Optional (default : False) | false, f, False, true, t, True |
| fields | Form fields | Optional | Stringified JSON |

Format for `fields`

```bash
[{
  "name": "str",
  "description": "str",
  "category": "str",
  "fields": [
    {
      "name": "str",
      "field_type": "Number",
      "is_array": boolean,
      "fill_by_search": boolean,
      "description": "str"
    }
  ],
  "is_searchable": boolean,
  "is_shared": boolean
}]

## Example stringified version for CLI

"[{\n  \"name\": \"MICROSOFT FORM\",\n  \"description\": \"A form for microsoft\",\n  \"category\": \"ANNUAL REPORT\",\n  \"fields\": [\n    {\n      \"name\": \"Cost of revenue\",\n      \"field_type\": \"Number\",\n      \"is_array\": false,\n      \"fill_by_search\": false,\n      \"description\": \"Extract cost of revenue\"\n    }\n  ],\n  \"is_searchable\": false,\n  \"is_shared\": false\n}]"
```

| **Key** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| name | Name of the Entity | Required |  |
| field_type | The data type of the entity | Required | "Number", "Date", "Text", "Table” |
| description | A short instruction to the prompt about the field | Optional |  |
| is_array | If it’s an entity with multiple values | Optional (default: False) | True, False |
| fill_by_search | Use internet search to fill this information | Optional (default: False | True, False |

**Response:**

```bash
{
   "category":"SECURITIES AND EXCHANGE COMMISSION",
   "created_at":"2024-09-25T09:13:50Z",
   "description":"",
   "fields":[
      {
         "description":"",
         "field_type":"Date",
         "fill_by_search":false,
         "is_array":false,
         "name":"testEnitity1"
      }
   ],
   "id":"66f3d44eeb87303bc52bb9b4",
   "is_searchable":false,
   "is_shared":false,
   "name":"test",
   "user_id":"google-oauth2|117349365869611297391"
}
```

---

### Filter form instances

A search query for retrieving form instances.

```bash
python3 documents/forms/filter_form_instances.py --scope all_documents --status "DONE" --category "SECURITIES AND EXCHANGE COMMISSION"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| scope | The scope of search | Required |  "all_documents",
"current_document",
"my_documents",
"shared_documents" |
| status | Status of workflow | Optional | "NOT_STARTED", "IN_PROGRESS", "DONE", "FAILED” |
| category | Category of  | Optional |  |
| query | When applied, string matches category | Optional |  |
| form_id | Form identifier | Optional |  |
| doc_id | Document identifier | Optional |  |
| only_latest | Fetches only latest | Optional (default True) |  |
| skip | Number of documents to skip | Optional (default 0) |  |
| limit | Max number of documents | Optional (default 25) |  |
| all | If set to true, all instances are fetched | Optional (default : False) |  |

**Response:**

```bash
{
   "total":4,
   "form_instances":[
      {
         "form_instance":{
            "data":[
               {
                  "name":"testEnitity1",
                  "value":"2023-08-03T00:00:00",
                  "identifier":"1f929c08-655e-4cf2-845c-18e3eb428ce7",
                  "weav_page_number":24
               }
            ],
            "metadata":{
               "modified_at":"2024-09-25T22:09:52.016000",
               "status":"DONE"
            }
         },
         "doc_id":"66e0fba3089fbd21c4dd80c3",
         "form_id":"66f3d44eeb87303bc52bb9b4",
         "file_name":"AAPL_10Q.pdf",
         "status":"AI_READY",
         "category":"SECURITIES AND EXCHANGE COMMISSION",
         "in_folders":[
            "66e0f93093798ee1c937e39a"
         ],
         "owner_id":"google-oauth2|117349365869611297391"
      },
      .
      .
      .
      .
   ]
}
```

---

### Execute form analytics

Running analytics on a form.

```bash
python3 documents/forms/execute_form_analytics.py --form_id 66f3d44eeb87303bc52bb9b4 --skip 0 --limit 25
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| skip | Number of documents to skip | Optional (default 0) |
| limit | Total number of documents to consider | Optional (default 25) |
| form_id | Form Identifier | Required |
| query | This is a mongo pipeline query that is fetched from the Search service. (default:  "{\n    'reason_for_no_pymongo_pipeline': 'No user request provided'\n}”) | Optional |

**Response:**

```bash
{
   "columns":[
      "Net Sales",
      "Total sales"
   ],
   "results":[
      {
         "Net Sales":[
            81797.0,
            82959.0,
            .
            .
            .
            .
         ],
         "metadata":{
            "_id":"66fe1b65b1d0dfb13c9975f0",
            "file_name":"AAPL_10Q.pdf",
            "in_folders":[
               
            ]
         }
      },
      {
         "Net Sales":[
            81797.0,
            82959.0,
            .
            .
            .
            .
         ],
         "Total sales":94569.0,
         "metadata":{
            "_id":"66fe29e1eb87303bc52bba93",
            "file_name":"AAPL_10Q.pdf",
            "in_folders":[
               
            ]
         }
      }
   ],
   "summary":"",
   "total_count":2
}
```

---

### Download query result

```bash
python3 documents/forms/download_query_result.py --form_id 66f3d44eeb87303bc52bb9b4 --download_format "JSON" 
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| form_id | Form Identifier | Required |  |
| query | This is a mongo pipeline query that is fetched from the Search service. (default:  "{\n    'reason_for_no_pymongo_pipeline': 'No user request provided'\n}”) | Optional |  |
| download_format | The format in which the results need to be viewed | Optional (default : “JSON”) | JSON, CSV |

**Response:**

`--download_format = "JSON"`

```bash
{'docs': [{'testEnitity1': '2023-08-03T00:00:00'}]}
```

`--download_format = "CSV"`

```bash
          testEnitity1
0  2023-08-03T00:00:00
```

---

---

## **Documents**

### Create document

Upload a document from your local system to the copilot. Has the ability to upload documents into a folder.

```bash
python3 documents/documents/create_document.py --file_path "AAPL_10Q.pdf"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| file_path | The file path to your document on your local system | Required |
| folder_id | The ID of the folder that should hold the document. If it is not provided, the file will be uploaded but will not be inside any folder. | Optional |

**Response:**

Upon uploading, the document response should be as follows.

```bash
{
   "ai_tags":[
      
   ],
   "category":"",
   "created_at":datetime.datetime(2024, 10, 3, 22, 14, 10, tzinfo=TzInfo(UTC)),
   "download_url":"/doc-proc-service/local_store/google-oauth2|117349365869611297391/66ff1732927ce8c0ebda42bd/66ff1732927ce8c0ebda42bd",
   "file_name":"AAPL_10Q.pdf",
   "form_instances":"None",
   "id":"66ff1732927ce8c0ebda42bd",
   "in_folders":[
      
   ],
   "media_type":"application/pdf",
   "pages":[
      
   ],
   "redacted_summary":"",
   "size":654929,
   "source":"application",
   "status":"NEW",
   "step_status":{
      "FORM_EXTRACTION":{
         "error":"",
         "modified_at":datetime.datetime(2024, 10, 3, 22, 14, 10, tzinfo=TzInfo(UTC)),
         "response":{
            
         },
         "status":"NOT_STARTED"
      }
   },
   "summary":"",
   "summary_status":"",
   "tags":[
      
   ],
   "tenant_id":"",
   "user_id":"google-oauth2|117349365869611297391"
}
```

After the document has been uploaded, it undergoes `process_document_sensors`  workflow which may take a while. 

Once the processing is completed, you will notice that some fields from before are updated using information extracted from the document using the `Get Document` API

---

### Get Document

Retrieve information about the uploaded document. Fields in this response might be empty initially but are completely filled once basic processing is completed

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| document_id | The unique identifier of the document | Required |
| fill_pages | If false pages will be empty | Optional (default: False) |

**Response:**

```bash
{
   "id":"66ff1732927ce8c0ebda42bd",
   "media_type":"application/pdf",
   "download_url":"/doc-proc-service/local_store/google-oauth2|117349365869611297391/66ff1732927ce8c0ebda42bd/66ff1732927ce8c0ebda42bd",
   "pages":[
      
   ],
   "status":"AI_READY",
   "file_name":"AAPL_10Q.pdf",
   "created_at":"",
   "size":654929,
   "source":"application",
   "category":"UNITED STATES SECURITIES AND EXCHANGE COMMISSION",
   "summary":"",
   "redacted_summary":"",
   "summary_status":"",
   "step_status":{
      "FORM_EXTRACTION":{
         "status":"DONE",
         "modified_at":"",
         "error":"",
         "response":{
            "name":"New",
            "category":"UNITED STATES SECURITIES AND EXCHANGE COMMISSION",
            "description":"A Test form",
            "fields":[
               {
                  "identifier":"4b68933c-2432-4784-8b01-37a1803b72a0",
                  "name":"new",
                  "field_type":"Number",
                  "description":"",
                  "is_array":true,
                  "fill_by_search":false,
                  "value":[
                     "0.00001",
                     "1.375",
                     .
                     .
                  ],
                  "weav_page_number":[
                     0,
                     0,
                     0,
                     0,
                     0,
                     .
                     .
                  ]
               }
            ],
            "is_shared":false,
            "is_searchable":false,
            "_id":"66ff076db1d0dfb13c99760f",
            "user_id":"google-oauth2|117349365869611297391",
            "created_at":"2024-10-03T21:06:53Z",
            "form_id":"66ff076db1d0dfb13c99760f"
         }
      }
   },
   "in_folders":[
      
   ],
   "tags":[
      
   ],
   "ai_tags":[
      
   ],
   "user_id":"google-oauth2|117349365869611297391",
   "tenant_id":"",
   "form_instances":"None"
}
```

<aside>
💡

You can observe that fields like `category` are updated once processing has finished.

</aside>

---

### Download form instance

Allows the user to download the extracted form

```bash
python3 documents/documents/download_form_instance.py --download_format "JSON" --document_id "66ff1732927ce8c0ebda42bd"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| document_id | The unique identifier of the document | Required |  |
| download_format | The format in which the results need to be viewed | Optional (default : “JSON”) | JSON, CSV |

**Response:**

`--download_format = "JSON"`

```bash
{
   "doc_id":"66ff1732927ce8c0ebda42bd",
   "form_id":"66ff076db1d0dfb13c99760f",
   "new":[
      "0.00001",
      "1.375",
      "0.000",
      .
      .
      .
    ]
}
```

`--download_format = "CSV"`

```bash
                     doc_id                   form_id                                                new
0  66ff1732927ce8c0ebda42bd  66ff076db1d0dfb13c99760f  ['0.00001', '1.375', '0.000', '0.875', '1.625'...
```

<aside>
💡

Downloading form instance can only be done once form processing has been completed and form definition has been created.

</aside>

<aside>
💡

If form processing has not been run, you can run it by first [creating a form definition](https://www.notion.so/How-to-use-the-Developer-Scripts-10c5084286c5801bb388fbcc98dc5626?pvs=21) and using the [Run workflow](https://www.notion.so/How-to-use-the-Developer-Scripts-10c5084286c5801bb388fbcc98dc5626?pvs=21) script by passing `workflow_name` as `process_form_workflow` 

</aside>

---

### Get document categories

Retrieves a list of all categories present on the copilot, considering categories from all documents.

```bash
python3 documents/documents/get_document_categories.py
```

**Response:**

```bash
{
   "categories":[
      "ANNUAL REPORT",
      "SECURITIES AND EXCHANGE COMMISSION",
      "UNITED STATES SECURITIES AND EXCHANGE COMMISSION"
   ]
}
```

---

### Get document tags

Retrieves a list of all tags present on the copilot, considering tags from all documents.

```bash
python3 documents/documents/get_document_tags.py
```

**Response:**

```bash
{'tags': [['apple']]}
```

---

### Get document page level status

Retrieves count of pages on which workflow has succeeded or failed.

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| document_id | The unique identifier of the document | Required |

**Response:**

```bash
{
   "classification":{
      "pages_done":25,
      "pages_failed":0
   },
   "entity_extraction":{
      "pages_done":25,
      "pages_failed":0
   },
   "ocr":{
      "pages_done":25,
      "pages_failed":0
   },
   "vectorization":{
      "pages_done":25,
      "pages_failed":0
   }
}
```

---

### Get page text and words

Retrieves information about words and text in a single page of the document.

```bash
python3 documents/documents/get_page_text_and_words.py --document_id 66f9ccbb927ce8c0ebda4261 --page_number 1
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| document_id | The unique identifier of the document | Required |
| page_number | The page number for which the information is required | Required |

**Response:**

```bash
{
   "page_number":1,
   "media_type":"NONE",
   "page_text":"9/6/23, 9:57 AM\naapl-20230701\nIndicate by check mark whether the Registrant has submitted electronically every Interactive Data File required to be submitted pursuant to Rule 405 of Regulation S-T (§232.405 of this chapter) during the preceding 12 months (or for such shorter period that the Registrant was required to submit such files).\nYes :selected: :unselected: No\nIndicate by check mark whether the Registrant is a large accelerated filer, an accelerated filer, a non-accelerated filer, a smaller reporting company, or an emerging growth company. See the definitions of \"large accelerated filer,\" \"accelerated filer,\" \"smaller reporting company,\" and \"emerging growth company\" in Rule 12b-2 of the Exchange Act.\nLarge accelerated filer :selected:\nAccelerated filer :unselected:\nNon-accelerated filer :unselected:\nSmaller reporting company :unselected:\nEmerging growth company :unselected:\nIf an emerging growth company, indicate by check mark if the Registrant has elected not to use the extended transition period for complying with any new or revised financial accounting standards provided pursuant to Section 13(a) of the Exchange Act. :unselected:\nIndicate by check mark whether the Registrant is a shell company (as defined in Rule 12b-2 of the Exchange Act). :unselected: Yes :selected: No\n15,634,232,000 shares of common stock were issued and outstanding as of July 21, 2023.\nhttps://www.sec.gov/Archives/edgar/data/320193/000032019323000077/aapl-20230701.htm\n2/31",
   "status":"NONE",
   "classification":{
      "page_class":"Company Regulatory Compliance",
      "page_sections":[
         "Interactive Data File Submission",
         "Company Classification",
         "Emerging Growth Company Status",
         "Shell Company Status",
         "Common Stock Issuance"
      ],
      "page_no":2
   },
   "extracted_entities":[
      {
         "entity_group":"default",
         "entities":[
            {
               "polygon":[
                  
               ],
               "key":"Date",
               "value":"9/6/23, 9:57 AM",
               "label":"Document Date",
               "is_sensitive":false
            },
            {
               "polygon":[
                  
               ],
               "key":"Document ID",
               "value":"aapl-20230701",
               "label":"Document Identifier",
               "is_sensitive":false
            },
            .
            .
            .
         ]
      }
   ],
   "redacted_summary":"",
   "words":[
      {
         "content":"9/6/23,",
         "polygon":[
            {
               "x":71.0,
               "y":42.0
            },
            .
            .
         ],
         "span":{
            "offset":0,
            "length":7
         },
         "confidence":0.994
      },
      .
      .
      .
   ]
}
```

---

### Get Page

Retrieves all the information from a single page of a document

```bash
python3 documents/documents/get_page.py --document_id 66f9ccbb927ce8c0ebda4261 --page_number 1
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** | **Allowed values** |
| --- | --- | --- | --- |
| document_id | The unique identifier of the document | Required |  |
| page_number | The page number for which the information is required | Required |  |
| bounding_boxes | Get information about bounding boxes polygons | Optional | false, f, False, true, t, True |

**Response:**

```bash
{
   "classification":{
      "page_class":"Company Regulatory Compliance",
      "page_no":2,
      "page_sections":[
         "Interactive Data File Submission",
         "Company Classification",
         "Emerging Growth Company Status",
         "Shell Company Status",
         "Common Stock Issuance"
      ]
   },
   "download_url":"/doc-proc-service/local_store/google-oauth2|117349365869611297391/66ff1732927ce8c0ebda42bd/1.jpg",
   "extracted_entities":[
      {
         "entities":[
            {
               "is_sensitive":false,
               "key":"Date",
               "label":"Document Date",
               "polygon":[
                  [
                     [
                        {
                           "x":71.0,
                           "y":42.0
                        },
                        {
                           "x":135.0,
                           "y":43.0
                        },
                        {
                           "x":136.0,
                           "y":66.0
                        },
                        {
                           "x":71.0,
                           "y":66.0
                        }
                     ]
                  ],
                  [
                     [
                        {
                           "x":140.0,
                           "y":43.0
                        },
                        {
                           "x":180.0,
                           "y":43.0
                        },
                        {
                           "x":180.0,
                           "y":66.0
                        },
                        {
                           "x":140.0,
                           "y":66.0
                        }
                     ]
                  ],
                  [
                     [
                        {
                           "x":185.0,
                           "y":43.0
                        },
                        {
                           "x":212.0,
                           "y":42.0
                        },
                        {
                           "x":212.0,
                           "y":66.0
                        },
                        {
                           "x":185.0,
                           "y":66.0
                        }
                     ]
                  ]
               ],
               "value":"9/6/23, 9:57 AM"
            },
            .
            .
            .
         ],
         "entity_group":"default"
      }
   ],
   "media_type":"image/jpeg",
   "page_hierarchy":"None",
   "page_number":1,
   "page_text":"Indicate by check mark whether the Registrant has submitted electronically every Interactive Data File required to be ....",
   "redacted_summary":"The document, identified as 'aapl-20230701', was ... ",
   "sensitive_words":[
      
   ],
   "status":"VECTORIZATION_DONE",
   "step_status":{
      "OCR":{
         "error":"",
         "modified_at":datetime.datetime(2024, 10, 3, 22, 14, 48, tzinfo=TzInfo(UTC)),
         "response":{
            
         },
         "status":"DONE"
      },
      "classification":{
         "error":"",
         "modified_at":datetime.datetime(2024, 10, 3, 22, 15, 33, tzinfo=TzInfo(UTC)),
         "response":{
            
         },
         "status":"DONE"
      },
      "entity_extraction":{
         "error":"",
         "modified_at":datetime.datetime(2024, 10, 3, 22, 16, 47, tzinfo=TzInfo(UTC)),
         "response":{
            
         },
         "status":"DONE"
      },
      "vectorization":{
         "error":"",
         "modified_at":datetime.datetime(2024, 10, 3, 22, 17, 42, tzinfo=TzInfo(UTC)),
         "response":{
            
         },
         "status":"DONE"
      }
   },
   "summary":"The document, identified as 'aapl-20230701', was submitted on..."
}
```

---

### Trigger document summary

Requests the copilot to generate a summary for a document. The response changes based on the state of the summarization workflow. Once the summarization is completed, the script returns the summary.

```bash
python3 documents/documents/trigger_document_summary.py --document_id 66ff1732927ce8c0ebda42bd
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| document_id | The unique identifier of the document | Required |

**Response:**

```bash
{
   "summary_status":"PROCESSING",
   "summary":"",
   "redacted_summary":""
}
```

<aside>
💡

If this script is run again after summarization is completed, you should receive a different response as shown below

</aside>

```bash
{
   "summary_status":"READY",
   "summary":"Apple Inc.'s Q3 2023 ...",
   "redacted_summary":"Apple Inc.'s Q3 2023 ..."
}
```

---

### Get document summary status

Once the [document summary](https://www.notion.so/How-to-use-the-Developer-Scripts-10c5084286c5801bb388fbcc98dc5626?pvs=21) has been triggered, this script helps check the status of summarization for the document.

```bash
python3 documents/documents/get_document_summary_status.py --document_id 66fe1b65b1d0dfb13c9975f042.0
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| document_id | The unique identifier of the document | Required |

**Response:**

If the script returns the following:

```bash
{'message': 'Summarization not triggered'}
```

Follow [document summary](https://www.notion.so/How-to-use-the-Developer-Scripts-10c5084286c5801bb388fbcc98dc5626?pvs=21) script to trigger summarization.

Once the summarization is triggered, 

The same script should return:

```bash
{'redacted_summary': '', 'summary': '', 'summary_status': 'PROCESSING'}
```

Once processing is completed, the script should return

```bash
{
   "summary_status":"READY",
   "summary":"Apple Inc.'s Q3 2023 ...",
   "redacted_summary":"Apple Inc.'s Q3 2023 ..."
}
```

---

## Folders

### Create folder

Allows the user to create a folder that they can use to group documents together.

```bash
python3 documents/folders/create_folder.py --name "Bank docs" --description "BANKING DOCUMENT" --category "BANKING"
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| name | Name of the folder to be created | Required |
| category | The category of the entire folder | Optional |
| description | A description for the folder | Optional |

**Response:**

```bash
{
   "id":"66ff3b79eb87303bc52bbae4",
   "documents":"None",
   "document_ids":[
      
   ],
   "shared_with_users":{
      
   },
   "shared_with_groups":{
      
   },
   "name":"Bank docs",
   "category":"BANKING",
   "description":"BANKING DOCUMENT",
   "created_at":"2024-10-04T00:48:57Z",
   "modified_at":"2024-10-04T00:48:57.573312Z",
   "user_id":"google-oauth2|117349365869611297391",
   "tenant_id":"",
   "workflow":{
      "workflow_id":"process_document_sensors",
      "form_id":"",
      "workflow_params":{
         
      }
   }
}
```

---

### Get writable folders

Gets a list of all writable folders giving their `name` and `folder_id`

```bash
python3 documents/folders/get_writable_folders.py
```

**Response:**

```bash
{
   "folders":[
      {
         "id":"66ff3b79eb87303bc52bbae4",
         "name":"Bank docs"
      },
	    .
	    .
	    .
   ]
}
```

### Get folder definition

Gets all metadata about a folder. Also displays the IDs of documents present inside the folder.

```bash
python3 documents/folders/get_folder_definition.py --folder_id 66e0f93093798ee1c937e39aent
```

**Parameters:**

| **Parameter** | **Description** | **Required/Optional** |
| --- | --- | --- |
| folder_id | The unique identifier of the folder | Required |

**Response:**

```bash
{
   "category":"",
   "created_at":"2024-09-11T01:58:08Z",
   "description":"",
   "document_ids":[
      "66f9ccbb927ce8c0ebda4261",
      "66e0fba3089fbd21c4dd80c3"
   ],
   "documents":"None",
   "id":"66e0f93093798ee1c937e39a",
   "modified_at":"2024-10-04T01:01:05.011000",
   "name":"BANKING",
   "shared_with_groups":{
      
   },
   "shared_with_users":{
      
   },
   "tenant_id":"",
   "user_id":"google-oauth2|117349365869611297391",
   "workflow":{
      "form_id":"",
      "workflow_id":"process_document_sensors",
      "workflow_params":{
         
      }
   }
}
```