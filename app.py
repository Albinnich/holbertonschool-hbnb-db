import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['USE_DATABASE'] = True
app.config['DATABASE_TYPE'] = os.getenv('DATABASE_TYPE', 'sqlite')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL', 'sqlite:///development.db')
db = SQLAlchemy(app)

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

from models import User

if app.config['DATABASE_TYPE'] == 'sqlite' and app.config['ENV'] == 'development':
    with app.app_context():
        db.create_all()

# Example route for testing purposes
@app.route('/')
def index():
    return 'Hello, World!'

# Ensure tables are created
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
