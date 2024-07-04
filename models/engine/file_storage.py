import json
import os

class FileStorage:
    def __init__(self, file_path='data.json'):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump({}, f)

    def _read_data(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def _write_data(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

    def save_user(self, user):
        data = self._read_data()
        user_id = user.get('id', str(uuid.uuid4()))
        user['id'] = user_id
        data[user_id] = user
        self._write_data(data)

    def get_user(self, user_id):
        data = self._read_data()
        return data.get(user_id)

    def update_user(self, user_id, user_data):
        data = self._read_data()
        if user_id in data:
            data[user_id].update(user_data)
            self._write_data(data)

    def delete_user(self, user_id):
        data = self._read_data()
        if user_id in data:
            del data[user_id]
            self._write_data(data)
