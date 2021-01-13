from flask import Flask
from app.blueprint import blueprint
from app.modules import database, controller


def create_app():
    app = Flask(__name__)
    
    # accepts both /endpoint and /endpoint/ as valid URLs
    app.url_map.strict_slashes = False

    # register each active blueprint
    app.register_blueprint(blueprint, url_prefix="/")

    return app
