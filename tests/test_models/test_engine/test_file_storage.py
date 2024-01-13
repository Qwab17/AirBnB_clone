#!/usr/bin/python3
"""
    Module ti implement test cases for the
    FileStorage classes

"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test serializationa and deserialization"""
    def setUp(self):
        """Set up the FileStorage test case"""
        self.file_storage = FileStorage()
        self.file_path = self.file_storage._FileStorage__file_path

    def tearDown(self):
        """Clean up tasks"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test that all returns the __objects dictionary"""
        first = self.file_storage.all()
        second = self.file_storage._FileStorage__objects
        self.assertEqual(first, second)

    def test_new(self):
        """Test that new adds an object to __objects"""
        instance = BaseModel()
        self.file_storage.new(instance)
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, self.file_storage._FileStorage__objects)

    def test_save(self):
        """Test that save properly saves objects to file"""
        test_obj = BaseModel()
        self.file_storage.new(test_obj)
        self.file_storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test that reload correctly deserializes objects from file"""
        instance = BaseModel()
        self.file_storage.new(instance)
        self.file_storage.save()
        self.file_storage.reload()
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, self.file_storage.all())


if __name__ == '__main__':
    unittest.main()
