import wave
from flask import Flask, request, redirect, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('login.html')


@app.route("/home")
def mod():
    return render_template('home.html')



if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    app.run()
