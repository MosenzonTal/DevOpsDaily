import json
from usersAPI import hello, app
from unittest.mock import patch, Mock
import unittest
import usersAPI


class TestEndpoints(unittest.TestCase):

    def setUp(self):
        self.fake_json = ({
            "test_user": {
                "id": "test",
                "name": "Test User",
                "favorite_color": "Black"
            }
        })

    # (Test #0)
    def test_basic(self):
        response = app.test_client().get('/')
        assert response.get_data(as_text=True) == 'Hello! this is DevOpsDaily!'
        assert response.status_code == 200, "404 Not Found"

    # (Test #1) Accessing the /users URI should return self.fake_json without the user ID
    def test_getAllUsers(self):
        with patch('usersAPI.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = self.fake_json

            response = usersAPI.getAllUsers()
            self.assertEqual(response, json.dumps({
                "test_user": {
                    "name": "Test User",
                    "favorite_color": "Black"
                }
            }))

    # (Test #2) Accessing the /user/test_user URI should return exactly the same as the following:
    def test_searchUserByName(self):
        with patch('usersAPI.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = self.fake_json
            response = usersAPI.searchUserByName('test_user')
            self.assertEqual(response, json.dumps({
                "test_user": {
                    "id": "test",
                    "name2": "Test User",
                    "favorite_color": "Black"
                }
            }))

    # (Test #3) Accessing the /user/test_user123 URL should return HTTP code 404 as the user does not exist in the database.
    def test_isUserExist(self):
        with patch('usersAPI.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = self.fake_json
            response = usersAPI.searchUserByName('test_user123')
            self.assertEqual(response, 'HTTP code 404 - the user does not exist in the database')
