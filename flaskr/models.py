import datetime

from flask_security import (
    UserMixin,
    RoleMixin,
)

from flaskr.db import DB

roles_users = (
    DB.Table('roles_users',
             DB.Column('user_id', DB.Integer(), DB.ForeignKey('user.id')),
             DB.Column('role_id', DB.Integer(), DB.ForeignKey('role.id'))))

class Role(DB.Model, RoleMixin):
    id = DB.Column(DB.Integer(), primary_key=True)
    name = DB.Column(DB.String(80), unique=True)
    description = DB.Column(DB.String(255))

class User(DB.Model, UserMixin):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(255), unique=True)
    email = DB.Column(DB.String(255), unique=True)
    password = DB.Column(DB.String(255))
    active = DB.Column(DB.Boolean())
    confirmed_at = DB.Column(DB.DateTime())
    roles = DB.relationship('Role', secondary=roles_users,
                            backref=DB.backref('users', lazy='dynamic'))

class Post(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    author_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable=False)
    created = DB.Column(DB.DateTime(), nullable=False, default=datetime.datetime.utcnow)
    title = DB.Column(DB.TEXT(), nullable=False)
    body = DB.Column(DB.TEXT(), nullable=False)
    user = DB.relationship('User')
