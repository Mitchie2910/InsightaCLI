import typer


from insighta.services.storage import clear_credentials, load_credentials
from insighta.services.client import post
from insighta.services.login import login

auth_app = typer.Typer()


@auth_app.command("login")
def perform_login():
    typer.echo("Opening browser for login...")

    login()

    typer.echo("Logged in successfully")


@auth_app.command("logout")
def logout():
    try:
        res = post("/auth/logout")
        print(res.status_code)

        if res.status_code != 200:
            print(res.status_code)
            print("Failed to logout from server")
            raise typer.Exit()

    except Exception:
        print("Server unreachable, clearing local session only")

    # always clear local state
    clear_credentials()
    print("Logged out successfully")


@auth_app.command()
def whoami():
    
    creds = load_credentials()

    try:
        username = creds["username"]

    except Exception:
        print("No credentials")
        return

    typer.echo(username)

