from flask import Flask, render_template

app = Flask(__name__)

@app.route("/output")
def output():
	return render_template("home.html")

if __name__ == "__main__":
	app.run(host='localhost', debug=True)
