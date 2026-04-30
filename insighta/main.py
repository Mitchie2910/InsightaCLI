import typer
from insighta.auth import auth_app
from insighta.profiles import profiles_app

app = typer.Typer()

app.add_typer(auth_app, name="auth")
app.add_typer(profiles_app, name="profiles")

if __name__ == "__main__":
    app()