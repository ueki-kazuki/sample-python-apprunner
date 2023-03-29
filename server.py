from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def root():
    return render_template('server.html', env=os.environ)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
