import app, json
from app.exceptions.exceptions import *
from flask import Blueprint, jsonify, request
from functools import wraps
from app.resources.auth import token_required
import traceback

blueprint = Blueprint("blueprint", __name__)

def exceptions_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UserNotFound:
            return jsonify({'Desc': 'User not found'}),404
        except UserAlreadyExists:
            return jsonify({'Desc': 'User Already Exists'}),409
        except InvalidPasswordPolicy:
            return jsonify({'Desc': 'Invalid Password Policy'}),409
        except InvalidCredentials:
            return jsonify({'Desc': 'Unauthorized'}),403
        except InvalidParams:
            return jsonify({'Desc': 'Invalid Params'}),400
        except SecretNotLoaded:
            return jsonify({'Desc': 'Secret has not been loaded'}),400
        except Exception as e:
            return jsonify({'Desc': "There was an error"}), 500
    return wrapper

@blueprint.route("/ping")
def main():
    return "pong"

@blueprint.route("/user", methods=['POST'])
@exceptions_decorator
@token_required
def create_user(user):
    user_json = request.get_json()
    result = app.controller.create_user(user_json)
    return "OK", 201

@blueprint.route("/login", methods=['POST'])
@exceptions_decorator
def login():
    user_json = request.get_json()
    result = app.controller.login(user_json)
    return jsonify(result), 200