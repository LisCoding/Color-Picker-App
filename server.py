from flask import Flask, render_template, session, request, redirect, flash, url_for
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template("index.html", color ="")

@app.route('/response', methods=["POST"])
def response():
    red = request.form["red"]
    green = request.form["green"]
    blue = request.form["blue"]
    color = "rgb("+ red + "," + green + ","  + blue + ")"
    return render_template('index.html', color= color)
app.run(debug=True)
