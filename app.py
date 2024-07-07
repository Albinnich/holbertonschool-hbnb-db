import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, get_jwt
from dotenv import load_dotenv
from models import db, User
from auth import login

load_dotenv()

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
jwt = JWTManager(app)

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

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    return login()

# Example of a protected admin endpoint
@app.route('/admin/data', methods=['POST', 'DELETE'])
@jwt_required()
def admin_data():
    current_user_id = get_jwt_identity()
    claims = get_jwt()

    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403

    # Proceed with admin-only functionality
    # Example: perform actions like adding or deleting data
    return jsonify({"msg": "Admin operation successful"}), 200

# Ensure tables are created
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
