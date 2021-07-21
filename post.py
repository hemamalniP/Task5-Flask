from flask import Flask

app = Flask(__name__)


@app.route('/hello/', methods=['GET','POST'])
def home():
    return "<h1>GET API </h1><p> Create a post api using python flask</p>"

if __name__=='__main__':
	app.run()


