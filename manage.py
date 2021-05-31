from authorization.basic_auth import hash_plaintext_password
from api.config import cfg
from api.db.models.users import Users

import click

from pprint import pprint


HELP_CONTEXT = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=HELP_CONTEXT)
def manage():
    """
    Helper scripts deployment and management
    """
    pass


@manage.group()
def db():
    pass


@db.command()
@click.option("--username", prompt=True)
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
@click.option("--full-name", prompt=True)
@click.option("--email", prompt=True)
def make_admin_user(
    username: str,
    password: str, 
    full_name: str,
    email: str
):
    hashed_pw = hash_plaintext_password(password)
    user = {
        "username": username,
        "password_hash": hashed_pw,
        "email": email,
        "full_name": full_name,
        "admin": True
    }
    try:
        Users.insert(Users(**user)).run_sync()  # type: ignore
        response = Users.select().where(Users.username==username).run_sync()
        pprint(response[0])
    except Exception as e:
        print(e)


@db.command()
def drop_users():
    Users.delete(force=True).run_sync()


if __name__ == "__main__":
    manage()
