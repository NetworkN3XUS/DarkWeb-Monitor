#test code for the flask 

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "1214ewwf46"
@app.route("/hello")
def index():
    flash("What's ur name:")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("hi " + str(request.form['name_input']) + ", great to see you")
    return render_template("index.html")