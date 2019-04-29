import unittest
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from project.database_setup import Base, Game, Mcq
from project.project import app , engine
from flask import json, jsonify
from project.games import InstantiateDB


InstantiateDB()

class testGames(unittest.TestCase):

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
        self.assertIn(b'id' , result.data)
        self.assertIn(b'category' , result.data)
        self.assertIn(b'name' , result.data)

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

             #check result from server with expected data
            self.assertEqual(
                result.status_code,
                200
            )

    def test_select_mcq_questions(self):
        result = self.app.get('/game/1/mcq')

        self.assertIn(b'"game_id":1' , result.data)
        self.assertIn(b'questions' , result.data)
        self.assertIn(b'"Answer1"', result.data)
        self.assertIn(b'"Answer2"', result.data)
        self.assertIn(b'"Answer3"', result.data)
        self.assertIn(b'"AnswerTrue"', result.data)


    def test_edit_questions(self):

        #testing put method
        sent = {"question_body": "GSDD", "Answer1": "2",
                "Answer2": "2", "Answer3": "1","AnswerTrue": "1"}
        result = app.test_client().put(
            '/game/1/mcq/2/edit',
            content_type='application/json',
            data=json.dumps(sent)
        )
        # check result from server with expected data
        self.assertEqual(
            result.status_code,
            200
        )
        self.assertEqual(b'{"message":"question promoted"}\n', result.data)


    def test_delete_game(self):
        result = app.test_client().delete(
            '/game/2/mcq/3/delete',
            content_type='application/json',
        )
        # check result from server with expected data
        self.assertEqual(
            result.status_code,
            200
        )
        self.assertEqual(b'{"message":"question deleted "}\n', result.data)


InstantiateDB()