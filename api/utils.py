def get_headers(token=None):
    headers = {
        "Content-Type": "application/json"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def extract_token(response):
    try:
        return response.json().get("token")
    except Exception:
        return None
