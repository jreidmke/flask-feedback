from unittest import TestCase
from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres4@localhost/feedback_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False

db.drop_all()
db.create_all()

class RegisterUserTestCase(TestCase):
    """Tests for new user"""

    def setUp(self):
        data = {'username': 'James', 'password': 'Pizza', 'email': 'jreidmke@gmail.com', 'first_name': 'James', 'last_name': 'Reid'}
        self.data = data
        self.first_name = data['first_name']

    def tearDown(self):
        data = {}

    def test_register_new_user(self):
        with app.test_client() as client:
            resp = client.post('/register', data = self.data, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'Welcome {self.first_name}!', html)