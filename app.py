from flask import Flask
from uuid import UUID



app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Neeraj Kumar, Welcome to the Flask application!"

@app.route("/user/<string:name>/<int:id>")
def user(name,id):
    return f"Hello {name} your id is {id}."


@app.route("/price/<float:amount>")
def price(amount):
    return f"Hello Neeraj Kumar your price is {amount}."


@app.route("/files/<path:file_path>")
def files(file_path):
    return f"Hello Neeraj Kumar your path is {file_path}."


@app.route("/student/<uuid:user_id>")
def student(user_id):
    return f"Hello Neeraj Kumar your user_id is {str(user_id)}."



# @app.route("/user/<name>")
# def user(name):
#     return f"Hello {name}, Welcome to the Contact Page!"


# @app.route("/student/<name>/<course>")
# def student(name,course):
#     return f"Hello {name}, Are you learning {course}!"

if __name__ == "__main__":
    app.run(debug=False)