import app, requests, json
from functools import wraps
from app.exceptions.exceptions import *
import os
import jwt

import datetime
from passlib.hash import pbkdf2_sha256 as sha256

def exceptions_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise
    return wrapper

try:
    import local_settings
    SECRET_KEY = local_settings.secret_key
except:
    SECRET_KEY = str(os.getenv("SECRET_KEY"))
    if not SECRET_KEY:
        raise SecretNotLoaded

class Controller():

    def __init__(self, database):
        self.db = database

    @exceptions_decorator
    def create_user(self, user_json):
        if not re.fullmatch(r'^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$', user_json["password"]):
            raise InvalidPasswordPolicy

        user_json["password"] = sha256.hash(user_json["password"])

        return self.db.create_user(user_json)

    @exceptions_decorator
    def login(self, user_json):
        logger.warning("ACA")
        try:
            user = self.db.get_user_by_username(user_json["username"])        
        except UserNotFound:
            raise InvalidCredentials
        if not sha256.verify(user_json["password"],user["password"]): 
            raise InvalidCredentials

        token_data = {'user':user_json["username"],'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=48)}
        token = jwt.encode(token_data,SECRET_KEY)
        
        return {'token':token}

    @exceptions_decorator
    def auth_user(self, user):
        try:
            user = self.db.get_user_by_username(user)
        except UserNotFound:
            raise InvalidCredentials
        return user        