import httpx
from insighta.services.get_tokens import get_valid_token

BASE_URL = "http://localhost:8080"


def headers():
    token = get_valid_token(refresh_token)
    api_version = 1

    base_headers = {
        "X-API-Version": str(api_version)
    }

    if token:
        base_headers["Authorization"] = f"Bearer {token}"

    return base_headers


def get(path: str, params : dict=None):
    return httpx.get(BASE_URL + path, params=params, headers=headers())


def post(path: str, json=None):
    url = BASE_URL + path
    print("➡️ Sending request to:", url)

    try:
        res = httpx.post(url, json=json, headers=headers(), timeout=10)
        print("⬅️ Got response")
        return res

    except Exception as e:
        print("Request failed:", repr(e))
        return None


def delete(path, json=None):
    return httpx.delete(BASE_URL + path, headers=headers())


def refresh_token(refresh_token):

    res1 = post(
        "/auth/refresh",
        json={"refresh_token": refresh_token})

    res1.raise_for_status()
    return res1.json()
