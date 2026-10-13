from flask import Flask, request
from uuid import UUID



app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Neeraj Kumar, Welcome to the Flask application!"

@app.route("/search")
def search():
    name = request.args.get("name","Guest")
    course = request.args.get("course","Unknown")
    return f"Hello {name}, Are you learning {course}."


if __name__ == "__main__":
    app.run(debug=False)