import unittest
import project
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Game, Mcq
from project import app , engine
from flask import json, jsonify

# DB Connection
engine = create_engine('sqlite:///testing.db')
Base.metadata.bind = engine

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
        #self.assertEquals(result.data , b'{"game":[{"category":"MCQ","id":1,"name":"mcq11"},'
                                       #b'{"category":"MCQ","id":2,"name":"mcq12"}]}\n')
        self.assertIn(b'"game"' , result.data)


    def test_ViewAGame(self):
        result = self.app.get('/game/2/mcq')
        self.assertIn( b'"game_id":2' , result.data)
    

    def test_AddNewGame(self):
             #send data as POST form to endpoint
            sent = { "name":"mcq13" , "category":"MCQ" }
            result = app.test_client().post(
                '/game/new',
                content_type='application/json',
                data=json.dumps(sent)
            )
            print(json.dumps(sent))
             #check result from server with expected data
            self.assertEqual(
                result.status_code,
                200
            )
