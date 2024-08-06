from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydb.sqlite3"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))  # اصلاح تایپی
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.username}"

@app.route('/')
def home():
    name = "matin"
    age = 19
    blogs = {"one": "blog one", "tow": "belog tow", "three": "belog three"}
    return render_template("pages/index.html", user=name, age=age, blogs=blogs)

@app.route("/about/")
def about():
    return render_template('pages/about.html')

@app.route('/user/<username>')
def say_hello(username):
    if username == "admin":
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('users', username=username))

@app.route('/admin')
def admin():
    return 'Welcome Admin!'

@app.route("/users/<username>")
def users(username):
    return f"hello user {username}"

@app.route("/login/", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        return f"Login page - username : {username} and email: {email}"

if __name__ == "__main__":  # درست کردن این خط
    with app.app_context():
        db.create_all()  # قرار دادن درون context
    app.run(host="localhost", debug=True)
