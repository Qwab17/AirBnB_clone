#!/usr/bin/python3
"""
    Module ti implement test cases for the
    FileStorage classes

"""
import unittest
import os
from models.engine.filestorage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Class to implement FileStorage test cases"""
    def setUp(self):
        """Prepares environment for test cases"""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Cleans up environment after each test case is complete"""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_save_and_reload(self):
        """Test serialization and deserialization"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

        self.storage._FileStorage__objects = {}
        self.storage.reload()

        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage._FileStorage__objects)
        first = obj.to_dict()
        second = self.storage._FileStorage__objects[key].to_dict()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
