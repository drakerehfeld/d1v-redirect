from flask import Flask,redirect
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return redirect("http://www.dayoneventures.com", code=302)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect("http://www.dayoneventures.com", code=302)
