import os

class DataManager:
    def __init__(self, use_database=False):
        self.use_database = use_database

    def save_user(self, user):
        if self.use_database:
            db.session.add(user)
            db.session.commit()
        else:
            self.save_user_to_file(user)

    def save_user_to_file(self, user):
        # Implement file-based save logic
        pass

# Initialize DataManager
use_database = os.getenv('USE_DATABASE', 'False').lower() in ('true', '1')
data_manager = DataManager(use_database=use_database)
