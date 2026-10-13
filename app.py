from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    is_logged_in = True
    marks = 9
    subject = ['Physics', 'Math', 'Python', 'Java']
    return render_template("index.html",is_logged_in=is_logged_in, marks=marks, subject=subject)

if __name__ == "__main__":
    app.run(debug=True)