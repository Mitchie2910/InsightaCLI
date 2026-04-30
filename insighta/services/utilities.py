import base64
import hashlib
import os
import secrets
import webbrowser
import requests
from insighta.services.storage import *

def open_auth_url(client_id, redirect_uri, state, challenge):
    url = (
        "https://github.com/login/oauth/authorize"
        f"?client_id={client_id}"
        f"&redirect_uri={redirect_uri}"
        f"&scope=read:user user:email"
        f"&state={state}"
        f"&code_challenge={challenge}"
        f"&code_challenge_method=S256"
    )

    webbrowser.open(url)

def generate_code_verifier(length=43):
    return base64.urlsafe_b64encode(os.urandom(length)).decode('utf-8').rstrip('=')



def generate_code_challenge(code_verifier: str):
    digest = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    print(len(base64.urlsafe_b64encode(digest).decode('utf-8').rstrip('=')))
    return base64.urlsafe_b64encode(digest).decode('utf-8').rstrip('=')

def generate_state():
    return secrets.token_urlsafe(16)


def exchange_code(code, verifier):
    response = requests.post(
        "http://localhost:8080/auth/token",
        json={
            "code": code,
            "code_verifier": verifier
        }
    )

    print(response.status_code)
    print(response.content)
    if response.status_code != 200:
        raise Exception("Auth failed")

    return response.json()


def persist(token_response):

    access_token = token_response.get("access_token")
    refresh_token = token_response.get("refresh_token")
    username = token_response.get("username")
    expires_at = token_response.get("expires_at")

    if not access_token:
        raise Exception("Missing access token in response")

    save_credentials({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "username": username,
        "expires_at": expires_at
    })

    return username

