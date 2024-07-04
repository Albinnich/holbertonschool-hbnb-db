import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_create_base_model(self):
        # Test creating an instance of BaseModel
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
