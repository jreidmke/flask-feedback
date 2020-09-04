from app import app
from models import db, User, Feedback

db.drop_all()
db.create_all()

user1 = User.register(username='James', password='Pizza', email='jreidmke@gmail', first_name='James', last_name='Reid')
user2 = User.register(username='Maria', password='Pizza', email='mariareidmke@gmail', first_name='Maria', last_name='Reid')
user3 = User.register(username='Oliver', password='Pizza', email='ollieg@gmail', first_name='Oliver', last_name='Germain')

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.commit()

fb1 = Feedback(title='Foo', content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', username='James')
fb2 = Feedback(title='Bar', content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', username='Maria')
fb3 = Feedback(title='Foo 2', content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', username='Oliver')

db.session.add(fb1)
db.session.add(fb2)
db.session.add(fb3)
db.session.commit()