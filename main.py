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

@app.route("/about_us")
def about_us():
    return render_template('about_us.html')


@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/quiz_maker")
def quiz_maker():
    return render_template('quiz_maker.html')


@app.route("/quiz")
def quiz():
    return render_template('quiz.html')


@app.route("/attemp")
def attemp():
    return render_template('attemp.html')







if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    app.run()
