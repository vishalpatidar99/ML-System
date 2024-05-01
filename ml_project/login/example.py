import requests
import json

oauth_server_url = "http://127.0.0.1:8000"

client_id = "3Q0M0OLUQRKLTgbzTT1Zl0SQw3dIhCy0byxmzfeW"
client_secret = "YUhgDY8tQVrUdcJKUoqjFwoNY6SHETbPIX75TXfpnkCioQ3XyzqDQmSuyPyYFCdzMloSV9pELl5zfJVRLmz8sTzNBis436jfdUMeT5TupomssDyFZqi63FKb69w9VAJi"
username = "groot"
password = "root"

def get_access_token():
    token_url = f"{oauth_server_url}/oauth/token/"
    data = {"grant_type": "password", "username": username, "password": password}
    auth = (client_id, client_secret)

    response = requests.post(token_url, data=data, auth=auth)

    if response.status_code == 200:
        access_token = response.json().get("access_token")
        return access_token
    else:

        print(f"Failed to obtain access token. Status code: {response.status_code}")
        print(response.text)
        return None
    
# Obtain an OAuth token
access_token = get_access_token()

if access_token:
    api_response = {"access_token": access_token}

    print("API Response:")
    print(json.dumps(api_response, indent=4))