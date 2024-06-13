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

def get_source_files(source_files_folder, upload_subfolders=False, ignore_files=[]):
    print(f"Getting files from {source_files_folder}")
    # check if the folder exists
    if not os.path.exists(source_files_folder):
        print(f"Folder {source_files_folder} does not exist.")
        return None

    # get a list of all files in the folder and subfolders
    if upload_subfolders:
        file_list = [os.path.join(root, file) for root, dirs, files in os.walk(source_files_folder) for file in files]
    else:
        file_list = [os.path.join(source_files_folder, file) for file in os.listdir(source_files_folder) if os.path.isfile(os.path.join(source_files_folder, file))]
    print(f"Files found: {file_list}")
    
    # If the file names contain any part of the string in ignore_files list, remove them
    if ignore_files:
        file_list = [file for file in file_list if not any(ignore in file for ignore in ignore_files)]

    return file_list

def upload_files(files_list, token, base_weav_url, destination_folder_id, allowed_file_types, folder_tags=False):
    
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
                print(f"Uploading file {file}")
                # print(os.path.basename(file))
                files = {"file_uploaded": (os.path.basename(file), f, 'application/pdf')}
                try:
                    response = requests.post(url, headers=headers, files=files, data=data)
                    print(response.json())
                    # print(response.status_code)
                    if response.status_code == 200:
                        print(f"File {file} uploaded successfully.")
                    else:
                        print(f"Error uploading file {file}. Status code: {response.status_code}")
                        print(response.json())
                        continue
                except Exception as e:
                    print(f"Error uploading file {file}. {e}\nSkipping....")
        except FileNotFoundError:
            print(f"File {file} not found. Skipping....")
        except Exception as e:
            print(f"Error opening file {file}. {e}\nSkipping....")
        
        # get the root directory and subdirectories as a list, and add them as tags
        if folder_tags:
            tags = os.path.dirname(file).split('/')
            tags = [tag for tag in tags if tag]
            tags_data = {"tags_to_add": tags}

            print(f"Tags: {tags}")

            # add tags to the file
            file_id = response.json().get('_id')
            patch_url = f"{base_weav_url}/file-service/documents/{file_id}/tags"
            patch_headers = {
                'accept': 'application/json',
                'Authorization': f"Bearer {token}",
                'Content-Type': 'application/json'
            }
            try:
                patch_response = requests.patch(patch_url, headers=patch_headers, json=tags_data)
                if patch_response.status_code == 200:
                    print(f"Tags added to file {file}")
                else:
                    print(f"Error adding tags to file {file}. Status code: {patch_response.status_code}")
                    print(patch_response.json())
            except Exception as e:
                print(f"Error adding tags to file {file}. {e}")        


def main():
    
    config = Config()
    try:
        token = config.get('token')
        base_weav_url = config.get('base_weav_url')
        destination_folder_id = config.get('destination_folder_id')
        allowed_file_types = config.get('allowed_file_types')
        source_files_folder = config.get('source_file_folder')
        upload_subfolders = config.get('upload_subfolders')
        folder_tags = config.get('folder_tags')
        ignore_files = config.get('ignore_files')
    except KeyError:
        print("Config file is missing required fields.\nIt should contain the following fields: token, base_weav_url, destination_folder_id, allowed_file_types")
        return
    
    source_files_list = get_source_files(source_files_folder, upload_subfolders, ignore_files)

    if source_files_list:
        upload_files(source_files_list, token, base_weav_url, destination_folder_id, allowed_file_types, folder_tags)

if __name__ == "__main__":
    main()