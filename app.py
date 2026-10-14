from flask import Flask, flash, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route("/login")
def login():
    session["user"] = "Neeraj"
    return "Login Successfull!!1"


@app.route("/dashboard")
def dashboard():
    user = session.get("user")
    if not user:
        return "Login First!!"
    
    return f"Welcome here, {user}";


@app.route("/logout")
def logout():
    session.pop("user",None)
    return "You Are Logged Out"
    
    






@app.route("/")
def home():
    is_logged_in = True
    marks = 9
    subject = ['Physics', 'Math', 'Python', 'Java']
    return render_template("index.html",is_logged_in=is_logged_in, marks=marks, subject=subject)


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/search")
# def search():
#     query = request.args.get("query")
#     return f"you are searching for : {query}"

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email").strip()
        age = request.form.get("age").strip()
        if not name:
            return "Name not provided"
        if not email:
            return "Email not provided"
        if not age.isdigit():
            return "Invalid age provided"
        
        flash("Registration Successful!!!!")
    return render_template("contact.html",name=name, email=email, age=age)

if __name__ == "__main__":
    app.run(debug=True)