## Process form tutorial

### Prerequisite:

### Document should be uploaded onto the co-pilot. If not uploaded, follow `upload_document.md` for instructions on how to upload the document.

### Document should have been processed with `process_document` workflow run successfully. If that's not done, follow `process_document.md` for instructions.

### Step 1: Create a form definition

In order to process a form. We first need to have a form definition.

```bash
python3 documents/forms/create_form.py --name "<form_name>" --category "<form_category>" --description "<form_description>" --fields "[{\\n  \\"name\\": \\"MICROSOFT FORM\\",\\n  \\"description\\": \\"A form for microsoft\\",\\n  \\"category\\": \\"ANNUAL REPORT\\",\\n  \\"fields\\": [\\n    {\\n      \\"name\\": \\"Cost of revenue\\",\\n      \\"field_type\\": \\"Number\\",\\n      \\"is_array\\": false,\\n      \\"fill_by_search\\": false,\\n      \\"description\\": \\"Extract cost of revenue\\"\\n    }\\n  ],\\n  \\"is_searchable\\": false,\\n  \\"is_shared\\": false\\n}]"

```

Remember to replace `<form_name>`, `<form_category>` and `<form_description>` with required values.

The `--fields` argument requires you to add entities to the forms such as details to look out for in the document during processing. It follows the following format:

```json
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

```

An example of this would be:

```json
[{
  "name": "ANNUAL REVENUE REPORT",
  "description": "This form describes the earnings for the financial year",
  "category": "ANNUAL REPORT",
  "fields": [
    {
      "name": "Total Revenue",
      "field_type": "Number",
      "is_array": False,
      "fill_by_search": False,
      "description": "Extract any fields of 'Total Revenue' that is found."
    },
    {
      "name": "Total Loss",
      "field_type": "Number",
      "is_array": False,
      "fill_by_search": False,
      "description": "Extract any fields of 'Total Loss' that is found."
    }
  ],
  "is_searchable": boolean,
  "is_shared": boolean
}]

```

To pass this into the shell as an argument for the script, we need to stringify the JSON:
It should look something like this:

```
"[{\\n  \\"name\\": \\"ANNUAL REVENUE REPORT\\",\\n  \\"description\\": \\"This form describes the earnings for the financial year\\",\\n  \\"category\\": \\"ANNUAL REPORT\\",\\n  \\"fields\\": [\\n    {\\n      \\"name\\": \\"Total Revenue\\",\\n      \\"field_type\\": \\"Number\\",\\n      \\"is_array\\": False,\\n      \\"fill_by_search\\": False,\\n      \\"description\\": \\"Extract any fields of 'Total Revenue' that is found.\\"\\n    },\\n    {\\n      \\"name\\": \\"Total Loss\\",\\n      \\"field_type\\": \\"Number\\",\\n      \\"is_array\\": False,\\n      \\"fill_by_search\\": False,\\n      \\"description\\": \\"Extract any fields of 'Total Loss' that is found.\\"\\n    }\\n  ],\\n  \\"is_searchable\\": boolean,\\n  \\"is_shared\\": boolean\\n}]"

```

In the response of this script, you will see that it holds an `id` field, which is the unique identifier of the form definition. Let's refer to this as `<form_id>`

### Step 1a (Optional): View the form definition

Once the form definition has been created, you can view it with

```bash
python3 documents/forms/get_form_definition.py --form_id "<form_id>"

```

### Step 2: Run the `process_form` workflow for a document

Now that the form definition is ready, we can run the `process_form` workflow for a document. To do so, run the following:

```bash
python3 workflows/run_workflow.py --doc_id "<document_id>" --workflow_name "process_form_workflow" --data "{\\"form_id\\":\\"<form_id>\\"}"

```

`<document_id>` is obtained after uploading the document and is the unique identifier of the document.<br>
`<form_id>` is obtained after creating the form definition in the previous step.
Similar to before, we need to stringify the JSON before passing it as an argument to the script.

### Step 3:

To check the status of the `process_form` workflow, run the following command:

```bash
python3 workflows/get_workflows_for_document.py --doc_id "<document_id>"

```

Alternatively, you can also use `run_id` and `workflow_id` to check the status of the workflow

```bash
python3 workflows/get_workflow_status.py --workflow_id "process_form" --workflow_run_id "<run_id>"

```

`<run_id>` and the `workflow_id` can be obtained from the response of `Step 2`

The `status` key from the response should tell you the current status of the workflow. Follow `Step 4` if the `status` says `failed`

### Step 4 (Optional)

If a workflow has failed, we might need to rerun it. To do so, run the following command:

```bash
python3 workflows/rerun_workflow.py --doc_id "<document_id>" --workflow_name "process_form" --data "{\\"form_id\\":\\"<form_id>\\"}"

```