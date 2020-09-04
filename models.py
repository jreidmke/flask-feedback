from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bc = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):

    __tablename__ = 'users'

    username = db.Column(db.String, unique = True, primary_key=True)
    password = db.Column(db.String, nullable = False)
    email = db.Column(db.String(50), nullable = False)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """Creates new user with hased password"""

        hashword = bc.generate_password_hash(password)

        hashword_utf8 = hashword.decode('utf8')

        return cls(username = username, password = hashword_utf8, email = email, first_name = first_name, last_name = last_name)