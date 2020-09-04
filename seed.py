from app import app
from models import db, User


db.drop_all()
db.create_all()

user1 = User.register(username='James', password='Pizza', email='jreidmke@gmail', first_name='James', last_name='Reid')
user2 = User.register(username='Maria', password='Pizza', email='mariareidmke@gmail', first_name='Maria', last_name='Reid')
user3 = User.register(username='Oliver', password='Pizza', email='ollieg@gmail', first_name='Oliver', last_name='Germain')

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

db.session.commit()