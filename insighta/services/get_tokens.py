from datetime import datetime, timezone

from insighta.services.storage import load_credentials, save_credentials, clear_credentials
from insighta.services.exceptions import LoginException



def get_valid_token(refresh_token):
    creds = load_credentials()
    expires_at = datetime.fromisoformat(
        creds["expires_at"].replace("Z", "+00:00")
    )

    if not creds:
        raise LoginException


    # still valid
    if expires_at > datetime.now(timezone.utc):
        return creds["access_token"]




    # expired → try refresh
    try:
        new_tokens = refresh_token(creds["refresh_token"])
        save_credentials(new_tokens)
        return new_tokens["access_token"]

    except Exception:
        # refresh failed → clean state
        clear_credentials()
        raise LoginException