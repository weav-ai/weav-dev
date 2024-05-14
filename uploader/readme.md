# Uploader

This is the files uploader for weav.ai.

## Configurations

You must specify the following configurations

{
    "config": {
        "source_file_folder": "path_to_your_files", # Mandatory
        "destination_folder_id": "1234", # Optional 
        "base_weav_url": "https://yourweavai.com", # Mandatory
        "token": "TOKEN", # Mandatory
        "allowed_file_types": ["pdf", "docx", "pptx", "xlsx", "txt", "jpg", "jpeg", "png", "csv"]
    }
}