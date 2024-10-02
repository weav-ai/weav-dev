import requests
import json
import argparse
import sys

class Config:
    def __init__(self, filename='config.json'):
        self.config = self.load_config(filename)

    def load_config(self, filename):
        with open(filename, 'r') as f:
            return json.load(f).get('config', {})

    def get(self, key):
        return self.config.get(key)

def init_db(domainname, token):
    """
    Send a POST request to initialize the database.
    
    Parameters:
        domainname (str): The domain name for the API endpoint.
        token (str): The bearer token for authorization.
    
    Returns:
        response: Response object from the requests library.
    """
    url = f"https://{domainname}/user-management-service/permissions/initdb"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.post(url, headers=headers)
    return response


def get_all_prompts(base_weav_url, token):
    """
    Fetch all prompts from the prompt management service.

    Parameters:
        domain (str): Domain name for the API endpoint.
        token (str): Bearer token for authorization.

    Returns:
        response: Response object from the requests library.
    """
    url = f"{base_weav_url}/prompt-management-service/prompts"
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        return None
    
    if response.status_code != 200:
        print(f"Error fetching prompts. Status code: {response.status_code}")
        print(response.json())
        sys.exit(1)

    prompt_list = []

    for prompt in response.json():
        prompt_list.append({
            'prompt_type': prompt['prompt_type'],
            'prompt_name': prompt['name'],
            'version_tag': prompt['version_tag'],
            'is_active': prompt['is_active']
        })

    return prompt_list


def get_prompt_details(base_weav_url, prompt_id, token, version_tag=None):
    """
    Fetch details of a specific prompt, optionally specifying a version tag.

    Parameters:
        domain (str): Domain name for the API endpoint.
        token (str): Bearer token for authorization.
        prompt_name (str): Name of the prompt.
        version_tag (str, optional): Specific version tag of the prompt, default is None.

    Returns:
        response: Response object from the requests library.
    """
    url = f"{base_weav_url}/prompt-management-service/prompts/{prompt_id}"
    if version_tag:
        url += f"?version_tag={version_tag}"
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        return None
    
    if response.status_code != 200:
        print(f"Error fetching prompt details. Status code: {response.status_code}")
        print(response.json())
        sys.exit(1)
    return response.json()

def deactivate_prompt(base_weav_url, prompt_id, token):
    """
    Change the status of a prompt to inactive.

    Parameters:
        domain (str): Domain name for the API endpoint.
        token (str): Bearer token for authorization.
        prompt_details (dict): Details of the prompt with modifications.

    Returns:
        response: Response object from the requests library.
    """

    prompt_details = get_prompt_details(base_weav_url, prompt_id, token)
    if not prompt_details:
        print(f"Prompt with ID {prompt_id} not found.")
        sys.exit(1)

    url = f"{base_weav_url}/prompt-management-service/prompts/"
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    # Modifying the prompt details
    prompt_details['is_active'] = False

    # Removing unnecessary fields
    for field in ['created_by', 'updated_by', 'created_at', 'updated_at']:
        prompt_details.pop(field, None)
    
    try:
        response = requests.put(url, headers=headers, json=prompt_details)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        return None
    
    if response.status_code != 200:
        print(f"Error fetching prompt details. Status code: {response.status_code}")
        print(response.json())
        sys.exit(1)

    return response.json()

def update_system_prompt(base_weav_url, prompt_id , new_version_tag, new_prompt_text, token):
    """
    Create a new version of a SYSTEM prompt with updated details.

    Parameters:
        domain (str): Domain name for the API endpoint.
        token (str): Bearer token for authorization.
        prompt_details (dict): Base details of the prompt from a previous version.
        new_version_tag (str): New version tag for the prompt.
        new_prompt_definition (str): Updated prompt definition.

    Returns:
        response: Response object from the requests library.
    """

    # get prompt details 
    prompt_details = get_prompt_details(base_weav_url, prompt_id, token=token)
    if not prompt_details:
        print(f"Prompt with ID {prompt_id} not found.")
        sys.exit(1)

    # deactivate the current prompt
    response = deactivate_prompt(base_weav_url, prompt_id, token=token)
    if not response:
        print(f"Error deactivating current version of prompt with ID {prompt_id}.")
        sys.exit(1)

    url = f"{base_weav_url}/prompt-management-service/prompts/"
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    # Updating prompt details for the new version
    prompt_details['version_tag'] = new_version_tag
    prompt_details['prompt_definition'] = new_prompt_text
    prompt_details['is_active'] = True

    # Removing unnecessary fields
    for field in ['id', 'created_by', 'updated_by', 'created_at', 'updated_at']:
        prompt_details.pop(field, None)
    
    try:
        response = requests.post(url, headers=headers, json=prompt_details)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        return None
    return response.json()


def main():
    parser = argparse.ArgumentParser(description='Manage prompts.')
    parser.add_argument('--action', type=str, choices=['get_all', 'get', 'deactivate', 'update'], help='Action to perform.')
    parser.add_argument('--prompt_text_file', type=str, help='prompt text file path')
    parser.add_argument('--prompt_id', type=str, help='Prompt ID.')
    parser.add_argument('--new_version_tag', type=str, help='New version tag for the prompt.')

    args = parser.parse_args()

    if args.action is None:
        print("No action specified. Please specify an action.")
        parser.print_usage()
        return

    if args.action in ('get', 'deactivate') and args.prompt_id is None:
        print(f"Please specify the prompt_id for action {args.action}") 
        parser.print_usage()
        return

    if args.action in ('update') and (args.prompt_id is None or args.prompt_text_file is None) :
        print(f"Please specify the prompt_id and prompt_text_file for action {args.action}") 
        parser.print_usage()
        return


    config = Config()
    try:
        token = config.get('token')
        base_weav_url = config.get('base_weav_url')
    except KeyError:
        print("Config file is missing required fields.\nIt should contain the following fields: token, base_weav_url, destination_folder_id, allowed_file_types")
        return    
        
    if args.action == 'get_all':
        response = get_all_prompts(base_weav_url, token=token)
    elif args.action == 'get':
        prompt_id = args.prompt_id
        response = get_prompt_details(base_weav_url, prompt_id, token=token)
    elif args.action == 'deactivate':
        prompt_id = args.prompt_id
        response = deactivate_prompt(base_weav_url, prompt_id, token=token)
    elif args.action == 'update':
        prompt_id = args.prompt_id
        new_version_tag = args.new_version_tag
        prompt_text_file = args.prompt_text_file     
        try:
            with open(prompt_text_file, 'r') as f:
                prompt_text = f.read()
        except FileNotFoundError:
            print(f"File {prompt_text_file} not found.")
            return
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return
        
        response = update_system_prompt(base_weav_url, prompt_id, new_version_tag, prompt_text, token=token)

    print(json.dumps(response, indent=4))

if __name__ == "__main__":
    main()
