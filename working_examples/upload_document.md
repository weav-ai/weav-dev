# Upload and retrieve document tutorial

## Step 1a

### Uploading document

To upload a document to the co-pilot, we can run the following command:

```bash
python3 documents/documents/create_document.py --file_path "file/path/on/local/file.pdf"

```

### **Alternatively, you can upload a document inside a folder.**

## Step 1b (Optional)

**Preqrequisite: A folder must be present in the co-pilot**<br>
If a folder is not present run the following first:<br>

```bash
python3 documents/documents/create_folder.py --name "<folder_name>" --category "<category>" --description "<description>"

```

Replacing `<category>`, `<description>` and `<folder_name>` as per your needs.

In the response of the above script, you will find a key called `id` which represents the unique identifier of the folder, let's refer to this as `<folder_id>`

Once this is done, you may run

```bash
python3 documents/documents/create_document.py --file_path "file/path/on/local/file.pdf" --folder_id "<folder_id>"

```

In the response of the script, you will find a key called `id` which represents the unique identifier of the document, let's refer to this as `<document_id>`

## Step 2a

### Retrieving document information

```bash
python3 documents/documents/get_document.py --document_id "<document_id>" --fill_pages True

```

## Step 2b

### Retrieving document information by page

```bash
python3 documents/documents/get_page_text_and_words.py --document_id "<document_id>" --page_number 1

```

`<document_id>` is retrieved from the response of Step 1.