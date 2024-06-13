# This python scripts takes a file path as input
import os
import requests
import argparse
import json

class Config:
    def __init__(self, filename='config.json'):
        self.config = self.load_config(filename)

    def load_config(self, filename):
        with open(filename, 'r') as f:
            return json.load(f).get('config', {})

    def get(self, key):
        return self.config.get(key)
    
def move_files(file_ids, token, base_weav_url, destination_folder_id):
    url = f"{base_weav_url}/file-service/folders/move/"
    print(f"Moving {file_ids} files to folder {destination_folder_id}")
    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {token}"
    }
    data = {
            "dest_folder_id": destination_folder_id,
            "file_ids": file_ids
            }
    
    try:
        response = requests.put(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print(f"{len(file_ids)} files moved successfully.")
        else:
            print(f"Error moving files. Status code: {response.status_code}")
            print(f"Response Text: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")

def main():

    # read the configuation file
    config = Config()
    try:
        base_weav_url = config.get('base_weav_url')
        token = config.get('token')
        destination_folder_id = config.get('destination_folder_id')
    except KeyError as e:
        print(f"A key error occurred: {e}")
        return None
    # parse the arguments

    try:
        parser = argparse.ArgumentParser(description='Move files from one folder to another')
        parser.add_argument('file_ids_list_file', type=str, help='Path of file with File ids to move')

        args = parser.parse_args()
        file_ids_list_file = args.file_ids_list_file
    except argparse.ArgumentError as e:
        print(f"An error occurred while parsing arguments: {e}")
        return None
    
    # read the file ids from the file
    try:
        with open(file_ids_list_file, 'r') as f:
            file_ids = f.read().splitlines()
    except FileNotFoundError:
        print(f"File {file_ids_list_file} not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

    # for each file id, move the file to the destination folder

    if len(file_ids) > 0:
        move_files(file_ids, token, base_weav_url, destination_folder_id)
    else:
        print(f"No file ids found in {file_ids_list_file}.")
        return None
    
        

# execute main function
if __name__ == "__main__":
    main()
    