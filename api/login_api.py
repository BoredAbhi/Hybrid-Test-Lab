import requests
from api.utils import get_headers

def login(base_url, username, password):
    url = f"{base_url}/api/login"
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=payload, headers=get_headers())
    return response
