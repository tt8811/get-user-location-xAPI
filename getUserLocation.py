from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env (if available)
load_dotenv('.env')

# Load environment variables from .env.local, which will override only missing variables from .env
load_dotenv('.env.local', override=True)

# Get environment variables
bearer_token = os.getenv('BEARER_TOKEN', False)
x_api_url = os.getenv('X_API_URL', False)
x_user_name = os.getenv('X_USER_NAME', False)

# Get user location method
def get_user_location(x_api_url, x_user_name, bearer_token):
    url = f"{x_api_url}/{x_user_name}"

    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }

    params = {
        "user.fields": "location"
    }

    # Make a request to the Twitter API
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'location' in data['data']:
            location = data['data']['location']
            print(f"UserName: '{x_user_name}' location: {location}")
        else:
            print(f"UserName: '{x_user_name}' does not have a location set.")
    else:
        print(f"Error: Unable to fetch data for user '{x_user_name}'. Status code: {response.status_code}")
        print(response.json())

get_user_location(x_api_url, x_user_name, bearer_token)
