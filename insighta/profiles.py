import typer


from insighta.services.client import get_valid_token, get, delete, post
from rich.table import Table
from rich.console import Console

profiles_app = typer.Typer()
console = Console(width=None)


@profiles_app.command("list")
def list_profiles(
    gender: str = None,
    country: str = None,
    min_age: int = None,
    max_age: int = None,
    sort_by: str = None,
    order: str = "asc",
    page: int = 1,
    limit: int = 10,
):

    params = {
        "gender": gender,
        "country": country,
        "min_age": min_age,
        "max_ge": max_age,
        "sort_by": sort_by,
        "order": order,
        "page": page,
        "limit": limit,
    }

    try:
        with console.status("Fetching profiles..."):
            res = get("/api/profiles", {k: v for k, v in params.items() if v is not None})
            res.raise_for_status()

        data = res.json()

    except Exception as e:
        console.print(f"Request Error {e}")
        return None

    table = Table(title="Profiles", expand=True)
    table.add_column("ID", no_wrap=True)
    table.add_column("Name", no_wrap=True)
    table.add_column("Name", no_wrap=True)
    table.add_column("Gender", no_wrap=True)
    table.add_column("Age", no_wrap=True)
    table.add_column("Age Group", no_wrap=True)
    table.add_column("Country Id", no_wrap=True)
    table.add_column("Gender Probability", no_wrap=True)
    table.add_column("Country Name", no_wrap=True)
    table.add_column("Country Probability", no_wrap=True)
    table.add_column("Created At")

    for p in data["data"]:

        table.add_row(
            str(p["id"]),
            str(p["name"],),
            str(p["gender"]),
            str(p["age"]),
            str(p["age_group"]),
            str(p["country_id"]),
            str(p["gender_probability"]),
            str(p["country_name"]),
            str(p["country_probability"]),
            str(p["created_at"]),
        )

    console.print(table)

@profiles_app.command()
def search(query: str):
    try:
        with console.status("Fetching profiles..."):
            res = get("/api/profiles/search",{"q": query})
            res.raise_for_status()

        data = res.json()

    except Exception as e:
        console.print(f"Request Error {e}. Login")
        return None


    table = Table(title="Profiles", expand=True)
    table.add_column("ID")
    table.add_column("Name", no_wrap=True)
    table.add_column("Gender", no_wrap=True)
    table.add_column("Age", no_wrap=True)
    table.add_column("Age Group", no_wrap=True)
    table.add_column("Country Id", no_wrap=True)
    table.add_column("Gender Probability", no_wrap=True)
    table.add_column("Country Name", no_wrap=True)
    table.add_column("Country Probability", no_wrap=True)
    table.add_column("Created At")

    for p in data["data"]:
        table.add_row(
            str(p["id"]),
            str(p["name"], ),
            str(p["gender"]),
            str(p["age"]),
            str(p["age_group"]),
            str(p["country_id"]),
            str(p["gender_probability"]),
            str(p["country_name"]),
            str(p["country_probability"]),
            str(p["created_at"]),
        )

    console.print(table)

@profiles_app.command("get")
def get_id(user_id: str):
    try:
        with console.status("Fetching profile..."):
            res = get(f"/api/profiles/{user_id}")
            res.raise_for_status()

        data = res.json()


    except Exception as e:
        console.print(f"Request Error {e}")
        return None

    table = Table(title="Profile", expand=True)
    table.add_column("ID", no_wrap=True)
    table.add_column("Name", no_wrap=True)
    table.add_column("Name", no_wrap=True)
    table.add_column("Gender", no_wrap=True)
    table.add_column("Gender Probability", no_wrap=True)
    table.add_column("Age", no_wrap=True)
    table.add_column("Age Group", no_wrap=True)
    table.add_column("Country Id", no_wrap=True)
    table.add_column("Country Name", no_wrap=True)
    table.add_column("Country Probability", no_wrap=True)
    table.add_column("Created At")

    p = data["data"]

    table.add_row(
        str(p["id"]),
        str(p["name"]),
        str(p["gender"]),
        str(p["age"]),
        str(p["age_group"]),
        str(p["country_id"]),
        str(p["gender_probability"]),
        str(p["country_name"]),
        str(p["country_probability"]),
        str(p["created_at"]),
    )

    console.print(table)
    return None


from pathlib import Path

@profiles_app.command("export")
def export(gender: str = None,
           country: str = None,
           min_age: str = None,
           max_age: str = None,
           sort_by: str = None,
           order: str = "asc",
           ):
    params = {
        "gender": gender,
        "country": country,
        "min_age": min_age,
        "max_age": max_age,
        "sort_by": sort_by,
        "order": order,
    }

    try:
        with console.status("Exporting CSV...."):
            res = get("/api/profiles/export", {k: v for k, v in params.items() if v is not None})
            res.raise_for_status()

        file_path = Path.cwd() / "profiles.csv"

        with open(file_path, "wb") as f:
            f.write(res.content)

        typer.echo(f"Exported to {file_path}")

    except Exception as e:
        console.print(f"Request Error {e}")
        return None

@profiles_app.command("delete")
def delete_profile(user_id: str):
    try:
        with console.status("Deleting profile..."):
            res = delete(f"/api/profiles/{user_id}")

            if res.status_code == 401 or res.status_code == 403:
                console.print("You are not authorized to delete this profile.")
                return None

            res.raise_for_status()

    except Exception as e:
        console.print(f"Request Error {e}")

@profiles_app .command("create")
def create_profile(name: str = typer.Option(...)):

    request_body = {"name": name}

    try:
        with console.status("Creating profile..."):
            res = post("/api/profiles",request_body )

            if res.status_code == 401 or res.status_code == 403:
                console.print("You are not authorized to create this profile.")
                return None

            res.raise_for_status()

            data = res.json()

            table = Table(title="Profiles", expand=True)
            table.add_column("ID")
            table.add_column("Name", no_wrap=True)
            table.add_column("Gender", no_wrap=True)
            table.add_column("Age", no_wrap=True)
            table.add_column("Age Group", no_wrap=True)
            table.add_column("Country Id", no_wrap=True)
            table.add_column("Gender Probability", no_wrap=True)
            table.add_column("Country Name", no_wrap=True)
            table.add_column("Country Probability", no_wrap=True)
            table.add_column("Created At")

            p = data["data"]

            table.add_row(
                str(p["id"]),
                str(p["name"]),
                str(p["gender"]),
                str(p["age"]),
                str(p["age_group"]),
                str(p["country_id"]),
                str(p["gender_probability"]),
                str(p["country_name"]),
                str(p["country_probability"]),
                str(p["created_at"]),
            )

            console.print(table)

    except Exception as e:
        console.print(f"Request Error {e}")


