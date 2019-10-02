import click
from flask import g
from flask.cli import with_appcontext
from flask_security import (
    LoginForm,
    RegisterForm,
    SQLAlchemyUserDatastore,
    Security,
)
from flask_security.forms import (
    email_required,
    Required,
    StringField,
)
from flask_security.core import current_user

from flaskr.models import User, Role
from flaskr import db
from flaskr.db import DB

security = Security()
user_datastore = SQLAlchemyUserDatastore(DB, User, Role)

class FlaskrLoginForm(LoginForm):
    # Note: clumsily overrides the default label for Email,
    # because I can't resolve the lazystring from get_form_field_label at instantiation time
    email = StringField("Username or Email", validators=[email_required])

class FlaskrRegisterForm(RegisterForm):
    username = StringField('Username', [Required()])


# In flaskr, this is added to auth.py. For flaskr-security,
# it's not needed, but saves some edits on the template.
def load_logged_in_user():
    """If the user is logged in, cache their user object to g.user."""
    if current_user.is_authenticated:
        g.user = current_user
    else:
        g.user = None


def initialize_tables():
    """Create any tables needed, if any."""
    DB.create_all()


def add_sample_user():
    """Create the flask-security sample user for debug purposes."""
    user_datastore.create_user(email='matt@nobien.net', password='password')
    DB.session.commit()


@click.command("add-sample-user")
@with_appcontext
def add_sample_user_command():
    """From the command line, create a sample user."""
    initialize_tables()
    add_sample_user()
    click.echo("Added sample user.")


def init_app(app):
    """Initialize SQLAlchemy and flask-security."""
    db.init_app(app)
    security.init_app(app, datastore=user_datastore,
                      login_form=FlaskrLoginForm,
                      register_form=FlaskrRegisterForm)

    # Initialize the tables on-load.
    with app.app_context():
        initialize_tables()

    # Register the "Add sample user" command to the CLI
    app.cli.add_command(add_sample_user_command)

    # Register the on-request callback.
    app.before_request(load_logged_in_user)
