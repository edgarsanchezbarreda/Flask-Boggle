from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    # TODO -- write tests for every view function / feature!
    def test_home(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('board', session)
            self.assertIsNone(session.get("highscore"))
            self.assertIsNone(session.get("nplays"))
            self.assertIn('Score:', html)
            self.assertIn('High Score:', html)

    def test_check_word(self):
        with self.client as client:
            with client.session_transaction() as session:
                session['board'] = [["A", "P", "P", "L", "E"],
                ["A", "P", "P", "L", "E"],
                ["A", "P", "P", "L", "E"],
                ["A", "P", "P", "L", "E"],
                ["A", "P", "P", "L", "E"]]
        res = self.client.get('/check-word?word=apple')
        self.assertEqual(res.json['result'], 'ok')
        
    def test_post_score(self):
        with self.client as client:
            with client.session_transaction() as session:
                session['highscore'] = 1
                self.assertEqual(session['highscore'], 1)
                session['nplays'] = 1
                self.assertEqual(session['nplays'], 1)
                self.assertIn('highscore', session)
                self.assertIn('nplays', session)