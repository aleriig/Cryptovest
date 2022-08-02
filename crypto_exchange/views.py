from flask import render_template

from . import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/purchase', methods=['GET', "POST"])
def buy():
    return "What would you like to buy?"

@app.route('/status', methods=['GET'])
def status():
    return "That's your current investment status"
