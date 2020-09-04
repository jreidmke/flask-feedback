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

    feedbacks = db.relationship('Feedback', cascade='all, delete', backref='user')

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """Creates new user with hased password"""

        hashword = bc.generate_password_hash(password)

        hashword_utf8 = hashword.decode('utf8')

        return cls(username = username, password = hashword_utf8, email = email, first_name = first_name, last_name = last_name)

    @classmethod
    def authenticate(cls, username, password):
        """Returns user object if password validated."""

        user = User.query.filter_by(username=username).first()

        if user and bc.check_password_hash(user.password, password):
            return user
        else:
            return False

class Feedback(db.Model):

    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.String, nullable = False)
    username = db.Column(db.String, db.ForeignKey('users.username', ondelete='cascade'))