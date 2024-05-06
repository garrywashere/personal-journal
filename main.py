from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)


class Pages(db.Model):
    pageid = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Float, nullable=False)
    title = db.Column(db.String(), nullable=False)
    body = db.Column(db.String(), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

def user_exists():
    pass

@app.route("/")
def index():
    return "index"

@app.route("/user/register")
def register():
    return "register"

@app.route("/user/login")
def login():
    return "login"

@app.route("/pages/new")
def new_page():
    return "new"

@app.route("/pages/view")
def view_page():
    return "view"

@app.route("/pages/edit")
def edit_page():
    return "edit"

@app.route("/pages/delete")
def delete_page():
    return "delete"

@app.route("/pages/search")
def search_page():
    return "search"

if __name__ == "__main__":
    import os

    if not os.path.exists("./instance/data.db"):
        with app.app_context():
            db.create_all()

    app.run("127.0.0.1", 8080, True)