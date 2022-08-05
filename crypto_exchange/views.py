from flask import render_template


from . import app
from .models import DBManager

ROUTE = 'data/cryptovest.db'

@app.route('/')
def home():
    db = DBManager(ROUTE)
    movements = db.query_SQL("SELECT * FROM cryptovest")
    return render_template("home.html", movs=movements)

@app.route('/buy', methods=['GET', "POST"])
def buy():
    
    return "What would you like to buy?"

@app.route('/status', methods=['GET'])
def status():
    return "That's your current investment status"
