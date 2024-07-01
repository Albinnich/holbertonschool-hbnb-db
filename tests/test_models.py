import unittest
from app import app, db, User, data_manager

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        user = User(id='1', email='test@example.com', password='password', is_admin=False)
        data_manager.save_user(user)
        
        if data_manager.use_database:
            db_user = User.query.get('1')
            self.assertIsNotNone(db_user)
            self.assertEqual(db_user.email, 'test@example.com')
        else:
            # Implement file-based validation logic
            pass

if __name__ == '__main__':
    unittest.main()
