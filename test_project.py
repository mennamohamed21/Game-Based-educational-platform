import unittest
import project
from project import app
from flask import json, jsonify


class testGamesRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        pass

    def test_games_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/games/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_games(self):
        result = self.app.get('/games/')
        print(result.data)
        self.assertEqual(result.data , b'{"game":[{"category":"MCQ","id":1,"name":"mcq11"},'
                                       b'{"category":"MCQ","id":2,"name":"mcq12"}]}\n')


    #class testGame(unittest.TestCase):
    #To test adding a new game
   # def test_add(self):


