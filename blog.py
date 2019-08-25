from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = 'f593ed484e91e4d32756d75c2d1b4163'

posts = [
    {
        "author": "Nate Stone",
        "title": "Post 1",
        "content": "Some stuff",
        "date_posted": "February 24, 2019"
    },
    {
        "author": "Nate Stone",
        "title": "Post 2",
        "content": "Some more stuff",
        "date_posted": "February 25, 2019"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def register():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
