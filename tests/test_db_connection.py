import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db

class TestDatabaseConnection(unittest.TestCase):
    def test_sqlite_connection(self):
        with app.app_context():
            self.assertTrue(db.session.execute('SELECT 1').fetchone())

    def test_postgresql_connection(self):
        # Implement your PostgreSQL connection test here
        pass

if __name__ == '__main__':
    unittest.main()
