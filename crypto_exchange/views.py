from . import app

@app.route('/')
def home():
    return "you are in the homepage"

@app.route('/purchase', methods=['GET', "POST"])
def buy():
    return "What would you like to buy?"

@app.route('/status', methods=['GET'])
def status():
    return "That's your current investment status"
