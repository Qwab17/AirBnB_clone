#!/usr/bin/python3
"""
    Module that implements test cases for the
    Amenity class

"""
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity instance created"""
    def test_instance(self):
        """Test attribute instances"""
        amenity = Amenity()
        self.assertIsInstance(amenity, State)
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertEqual(amenity.name, "")

    def test_attributes(self):
        """Verify instance attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_str_representation(self):
        """Test the __str__ method on State"""
        amenity = Amenity()
        expected_str = f"[Amenity] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(amenity.__str__(), expected_str)


if __name__ == "__main__":
    unittest.main()
