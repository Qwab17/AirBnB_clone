#!/usr/bin/python3
"""
    Module to implement test cases for the
    BaseModel class

"""
import unittest
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test case class for BaseModel base class"""
    def test_create_instance(self):
        """Test creation of new BaseModel instances"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_str_representation(self):
        """Test for the string formatting method"""
        inst = BaseModel()
        expected_str = f"[BaseModel] ({inst.id}) {inst.__dict__}"
        self.assertEqual(inst.__str__(), expected_str)

    def test_save(self):
        """Test the save method for all instances"""
        instance = BaseModel()
        old_save = instance.updated_at
        instance.save()
        self.assertNotEqual(old_save, instance.updated_at)

    def test_to_dict(self):
        """Tests instance convertion to dictionary"""
        instance = BaseModel()
        instance_dct = instance.to_dict()
        self.assertIsInstance(instance_dct, dict)
        self.assertEqual(instance_dct['__class__'], 'BaseModel')
        self.assertEqual(instance_dct['id'], instance.id)
        self.assertIsInstance(instance_dct['created_at'], str)
        self.assertIsInstance(instance_dct['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
