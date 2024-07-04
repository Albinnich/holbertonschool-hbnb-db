from . import db
from ..user import User

class DBStorage:
    def save_user(self, user):
        db.session.add(user)
        db.session.commit()

    def get_user(self, user_id):
        return User.query.get(user_id)

    def update_user(self, user_id, user_data):
        user = User.query.get(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            db.session.commit()

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
