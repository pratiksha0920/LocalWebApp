import flask

app=flask.Flask(__name__)


@app.route("/",methods=["GET"])
def home():
	return "Welcome"

@app.route("/mujahed", methods=["GET"])
def myfunc():
	return "Welcome <b>Mujahed</b>"

app.run()
#test