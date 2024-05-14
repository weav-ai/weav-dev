import requests
import json
import os

class Config:
    def __init__(self, filename='config.json'):
        self.config = self.load_config(filename)

    def load_config(self, filename):
        with open(filename, 'r') as f:
            return json.load(f).get('config', {})

    def get(self, key):
        return self.config.get(key)

def get_source_files(source_files_folder):
    print(f"Getting files from {source_files_folder}")
    # check if the folder exists
    if not os.path.exists(source_files_folder):
        print(f"Folder {source_files_folder} does not exist.")
        return None

    # get a list of all files in the folder
    return [os.path.join(source_files_folder, file) for file in os.listdir(source_files_folder)]

def upload_files(files_list, token, base_weav_url, destination_folder_id, allowed_file_types):
    
    print(f"files to upload: {files_list}")
    url = f"{base_weav_url}/file-service/documents/"
    # print(f"Uploading files to {url}")

    headers = {
    'accept': 'application/json',
    'Authorization': f"Bearer {token}"
    }
    data = {
        'folder_id': destination_folder_id
    }

    for file in files_list:
        # check if the file type is allowed
        if file.split('.')[-1] not in allowed_file_types:
            print(f"{file} : Invalid file type. Skipping.")
            continue
        try:
            with open(file, 'rb') as f:
                # print(f"Uploading file {file}")
                # print(os.path.basename(file))
                files = {"file_uploaded": (os.path.basename(file), f, 'application/pdf')}
                try:
                    response = requests.post(url, headers=headers, files=files, data=data)
                    # print(response.json())
                    # print(response.status_code)
                    if response.status_code == 200:
                        print(f"File {file} uploaded successfully.")
                except Exception as e:
                    print(f"Error uploading file {file}. {e}\nSkipping....")
        except FileNotFoundError:
            print(f"File {file} not found. Skipping....")
        except Exception as e:
            print(f"Error opening file {file}. {e}\nSkipping....")

def main():
    
    config = Config()
    try:
        token = config.get('token')
        base_weav_url = config.get('base_weav_url')
        destination_folder_id = config.get('destination_folder_id')
        allowed_file_types = config.get('allowed_file_types')
        source_files_folder = config.get('source_file_folder')
    except KeyError:
        print("Config file is missing required fields.\nIt should contain the following fields: token, base_weav_url, destination_folder_id, allowed_file_types")
        return
    
    source_files_list = get_source_files(source_files_folder)

    if source_files_list:
        upload_files(source_files_list, token, base_weav_url, destination_folder_id, allowed_file_types)

if __name__ == "__main__":
    main()