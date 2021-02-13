import wave
from flask import Flask, request, redirect, render_template


app = Flask(__name__)


@app.route("/")
def login():
    return render_template('login.html')


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/view_group")
def view_group():
    return render_template('view_group.html')

@app.route("/groups")
def groups():
    return render_template('groups.html')


@app.route("/quizzes")
def quizzes():
    return render_template('quizzes.html')



if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    app.run()
