from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Neeraj Kumar, Welcome to the Flask application!"

@app.route("/about")
def about():
    return "Hello Neeraj Kumar, Welcome to the About Page!"

@app.route("/contact")
def contact():
    return "Hello Neeraj Kumar, Welcome to the Contact Page!"

if __name__ == "__main__":
    app.run(debug=True)