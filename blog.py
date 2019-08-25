from flask import Flask, render_template
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
