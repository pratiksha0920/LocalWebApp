from flask import (
	Flask,
	render_template
)

app=Flask(__name__,template_folder="templates")

@app.route("/",methods=["GET"])
def home():
	return "Welcome HTML Based Flask App..."

@app.route("/megha", methods=["GET"])
def myfunc():
	return render_template("home.html")

app.run(host='0.0.0.0',port=5001)