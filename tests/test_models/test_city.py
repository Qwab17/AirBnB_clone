#!/usr/bin/python3
"""
    Module to implement test cases for the
    class City

"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Implement test cases for city instances"""
    def setUp(self):
        """Prepares environment for each test case"""
        self.city = City()

    def tearDown(self):
        """Cleans environment after each test case"""
        self.city = None

    def test_save_method(self):
        """Test the save method"""
        old_update = self.city.updated_at
        self.city.save()
        self.assertNotTrue(old_update, self.city.updated_at)

    def test_dictionary_keys(self):
        """Test keys from to_dict() method"""
        city_dct = self.city.to_dict()
        selt.assertIn('state_id', city_dct)
        selt.assertIn('name', city_dct)
        selt.assertIn('__class__', city_dct)
        selt.assertIn('id', city_dct)
        selt.assertIn('created_at', city_dct)
        selt.assertIn('updated_at', city_dct)

    def test_attributes(self):
        """Test instance attributes"""
        self.assertTrue(hasattr(self.city), 'state_id')
        self.assertTrue(hasattr(self.city), 'name')
        self.assertTrue(hasattr(self.city), '__class__')
        self.assertTrue(hasattr(self.city), 'id')
        self.assertTrue(hasattr(self.city), 'created_at')
        self.assertTrue(hasattr(self.city), 'updated_at')
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == "__main__":
    unittest.main()
