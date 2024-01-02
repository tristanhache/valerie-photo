from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/photo")
def index():
    return render_template("photos.html")

@app.route("/prix-promotions")
def index():
    return render_template("prix.html")