from flask import Flask,redirect
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return redirect("http://www.dayoneventures.com", code=301)
