import os
from flask import (
    Flask, render_template, request,
    redirect, url_for, session, flash)    
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__, static_url_path='/static')

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/register, "methods=["GET", "POST"
def register():
    return render_template("register.html")

@app.route('/add_route', methods=['GET', 'POST'])
def add_route():
    return render_template('add_route.html', title='add a route', form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '84.203.6.55'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)
