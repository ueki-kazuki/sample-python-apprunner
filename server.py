from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('server.html', env=os.environ, headers=request.headers)
