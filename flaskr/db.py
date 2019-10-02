import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


def init_db():
    """Clear existing data and create new tables."""
    DB.drop_all()
    DB.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    DB.init_app(app)
    app.cli.add_command(init_db_command)
