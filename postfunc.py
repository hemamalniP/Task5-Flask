from flask import Flask,request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    val1=int(request.args['a'])
    val2=int(request.args['b'])
    ans=val1+val2
    return str(ans)
    
if __name__=='__main__':
	app.run(debug=True)


