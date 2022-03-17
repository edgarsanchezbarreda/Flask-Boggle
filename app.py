from flask import Flask, request, render_template, redirect, session
from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY']='key'

@app.route('/')
def board():
    board = boggle_game.make_board()
    return render_template('index.html', board = board)