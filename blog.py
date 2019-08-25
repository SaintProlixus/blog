from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
    return "<h3>Hello World!</h3>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
