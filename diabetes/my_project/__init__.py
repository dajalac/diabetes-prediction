from flask import Flask
from config import Config


def create_app():
    server = Flask(__name__)
    server.config.from_object(Config)
    #register_dashapps(server)
    register_blueprints(server)
    return server


def register_blueprints(server):
    from my_project import login
    server.register_blueprint(login)

#def register_dashapps(app):
