import os

from flask import Flask
from flask_restx import Api

from src.api.db import init_db
from src.api.posts.views import ns as posts_namespace
from src.api.users.views import ns as users_namespace


def create_app():

    app = Flask(__name__)
    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)

    init_db(app.config["SQLALCHEMY_DATABASE_URI"])

    api = Api(
        app=app,
        version="1.0",
        title="Blog APIs",
        description="A simple Blog Post APIs",
        contact_email="yspuneeth1994@gmail.com",
    )

    api.add_namespace(posts_namespace, "/posts")
    api.add_namespace(users_namespace, "/users")

    return app
