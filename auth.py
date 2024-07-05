from flask import jsonify, request
from flask_jwt_extended import create_access_token
from models import User, bcrypt

def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    # Authenticate user
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        # Include role information in JWT claims
        additional_claims = {"is_admin": user.is_admin}
        access_token = create_access_token(identity=user.id, additional_claims=additional_claims)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Invalid credentials"}), 401
