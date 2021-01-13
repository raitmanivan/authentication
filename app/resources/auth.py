import app
from app.exceptions.exceptions import *
from functools import wraps
from flask import jsonify, request
import jwt
import os

try:
    import local_settings
    SECRET_KEY = local_settings.secret_key
except:
    SECRET_KEY = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
        raise SecretNotLoaded

def validar_token():
    auth_header = str(request.headers.get('Authorization'))
    if not auth_header or 'Bearer ' not in auth_header:
        return {'Desc': 'Unauthorized', 'code':403}
    try:
        split = auth_header.split(' ')
        decode_auth = jwt.decode(split[1],SECRET_KEY, algorithms=['HS256'])
    except:
        return {'Desc': 'Unauthorized', 'code':403}
    
    user_authenticated = app.controller.auth_user(decode_auth['user'])

    if not user_authenticated:
        return {'Desc': 'Unauthorized', 'code':403}

    return {'Desc':'Authenticated successfully','user':decode_auth['user']}
        
def token_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        res = validar_token()
        if not res.get('user'):
            return jsonify ({'Desc':res['Desc']}),401
        return func(res.get('user'),*args,**kwargs)
    return wrapper
