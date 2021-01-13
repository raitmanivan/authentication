from app.database.database import Database
from app.controller.controller import Controller

try:
    database = Database()
except:
    database = None

controller = Controller(database)
