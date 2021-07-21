from flask import Flask 

app = Flask(__name__)

@app.route('/default/<name>')
def get_default(name):
    return 'the value is:'+ name

if __name__=='__main__':
	app.run()



