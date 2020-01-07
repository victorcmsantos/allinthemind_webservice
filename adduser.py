import click
from app.models import User, Role
from app import db


@click.command()
@click.option('--username', prompt='Enter the username', help='The name of the user')
@click.option('--email', prompt='Enter the email of this user', help='Enter the email of this user')
@click.option('--password', prompt='Enter the password', confirmation_prompt=True, hide_input=True, help='The password of the user')
def useradd(username, email, password):
  u = User(username=username, email=email)
  u.set_password(password)
  db.session.add(u)
  db.session.commit()


if __name__ == '__main__':
  useradd()
