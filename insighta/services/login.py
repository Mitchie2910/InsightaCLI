from insighta.services.callbackserver import start_server
from insighta.services.utilities import *
import os


def login():
    client_id = os.getenv("GITHUB_CLIENT_ID")
    port = 8000
    redirect_uri = f"http://localhost:{port}/callback"

    state = generate_state()
    verifier = generate_code_verifier()
    challenge = generate_code_challenge(verifier)

    open_auth_url(client_id, redirect_uri, state, challenge)

    code, returned_state = start_server(port)

    print("code is " + code)
    print("stat is " + returned_state)

    if state != returned_state:
        raise Exception("Invalid state")
    
    tokens = exchange_code(code, verifier)

    username = persist(tokens)

    print(f"Logged in as @{username}")
    

