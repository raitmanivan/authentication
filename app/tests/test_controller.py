import app
import unittest
from unittest.mock import Mock
from app.exceptions.exceptions import *
from app.controller.controller import Controller
from app.database.database import Database

class ControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app().test_client()
        self.app.testing = True
        self.db = Database()
        self.controller = Controller(self.db)

    def test_create_user(self):
        self.db.create_user = Mock(return_value = True)
        result = self.controller.create_user({"username":"leotest","password":"Test123!"})
        self.assertEqual(True, result)

    def test_auth_user(self):
        self.db.get_user_by_username = Mock(return_value ={'username': 'leotest', 'id': 1, 'password': '$pbkdf2-sha256$29000$HyMEYCyFMIYwBuA8J6S0Ng$a439f3U1.KduUyKbnUOn0jePhb.8ZD62RTr9uUd4QBE'})
        result = self.controller.auth_user({"username":"leotest","password":"test"})
        self.assertEqual({'username': 'leotest', 'id': 1, 'password': '$pbkdf2-sha256$29000$HyMEYCyFMIYwBuA8J6S0Ng$a439f3U1.KduUyKbnUOn0jePhb.8ZD62RTr9uUd4QBE'}, result)

    def test_auth_user_not_found(self):
        self.db.get_user_by_username = Mock(side_effect = UserNotFound)
        self.assertRaises(InvalidCredentials, self.controller.auth_user, {"username":"leotest","password":"test"})