from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Neeraj Kumar, Welcome to the Flask application!"

if __name__ == "__main__":
    app.run(debug=True)