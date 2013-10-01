from flask import Flask
app = Flask(__name__)

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from os import environ

##
# MySQL connection parameters example:
#
#   OPENSHIFT_MYSQL_DB_HOST=524b2451234fa45614000004-caruccio.getup.io
#   OPENSHIFT_MYSQL_DB_PASSWORD=jef23dqf1fN_
#   OPENSHIFT_MYSQL_DB_PORT=43541
#   OPENSHIFT_MYSQL_DB_URL=mysql://adminF42DfaE:jef23dqf1fN_@524b2451234fa45614000004-caruccio.getup.io:43541/
#   OPENSHIFT_MYSQL_DB_USERNAME=adminF42DfaE
#
# Default database name is the app name itself:
#
#   OPENSHIFT_APP_NAME=flask
#
# To see your configuration, SSH into your app gear and execute 'env':
# 
#   $ rhc ssh [APP]
#   > env | grep MYSQL
#
##

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ['OPENSHIFT_MYSQL_DB_URL'] + environ['OPENSHIFT_APP_NAME']
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def index():
    users = []
    for user in User.query.all():
        users.append('{u.id}: <strong>{u.username}</strong> ({u.email})'.format(u=user))
    return '<br>'.join(users)

if __name__ == "__main__":
    app.run()

