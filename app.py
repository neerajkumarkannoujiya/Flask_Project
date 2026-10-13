from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    name = "Neeraj"
    age = 24
    address = "Noida"
    
    return render_template("index.html", name=name, age=age, address=address)

if __name__ == "__main__":
    app.run(debug=True)