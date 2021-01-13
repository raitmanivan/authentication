import datetime
import calendar
import os

from functools import wraps
from app.exceptions.exceptions import *
from sqlalchemy import create_engine,Column,String,BigInteger,Float,DateTime, and_, func, Boolean
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin

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
    DB_URL = local_settings.db_url
except:
    DB_URL = os.getenv("DB_URL")
    if not DB_URL:
        raise SecretNotLoaded
        
Base = declarative_base()

class User(Base, SerializerMixin):
    __tablename__ = "users"

    id = Column("id", BigInteger, primary_key=True)
    username = Column("username", String, unique=True)
    password = Column("password", String)

class Database():

    def __init__(self):
        self.db_url = DB_URL
        self.engine = create_engine(self.db_url, pool_recycle=3600)
        self.Session = sessionmaker(bind=self.engine)

    @exceptions_decorator
    def create_user(self, user_json):
        result = False
        session = self.Session()
        user = User()
        user.username = user_json["username"]
        user.password = user_json["password"]

        session.add(user)
        try:
            session.commit()
            result = True
        except IntegrityError:
            result = False
        session.close()
        
        return result

    @exceptions_decorator
    def get_user_by_username(self, username):
        user = self.Session().query(User).filter(User.username == username).first()
        self.Session().commit()
        self.Session().close()
        if user:
            return user.to_dict()
        else:
            raise UserNotFound
