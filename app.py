import os
from flask import (
    Flask, render_template, request,
    redirect, url_for, session, flash)    
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '84.203.6.55'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)