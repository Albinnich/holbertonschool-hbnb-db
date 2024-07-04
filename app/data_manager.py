import os
from .models import User

class DataManager:
    def __init__(self):
        self.use_database = os.getenv('USE_DATABASE', 'False').lower() in ['true', '1', 't']

    def save_user(self, user):
        if self.use_database:
            db.session.add(user)
            db.session.commit()
        else:
            pass

    def get_user_by_id(self, user_id):
        if self.use_database:
            return User.query.get(user_id)
        else:
            pass
