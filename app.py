from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['USE_DATABASE'] = True  # Switch between database and file-based storage
db = SQLAlchemy(app)

# Import models
from models import User

# Ensure tables are created
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
