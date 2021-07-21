from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>GET API </h1><p> Create a get api using python flask</p>"

app.run()

