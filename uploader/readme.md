# Uploader

This is the files uploader for weav.ai.

## Configurations

All configurations needed are in the file config.json. 

You must specify the following configurations

- source_file_folder
- base_weav_url
- token

You may specify

- destination_folder_id
- allowed_file_types
- upload_subfolder (default is true)
- folder_tags (add folder names as tags for documents)
- ignore_files (add strings that would ignore the files names that contain them. Case sensitive.)

## Running the uploader

The uploader runs with python 3.10 or above. 

python weav_ai_uploader.py