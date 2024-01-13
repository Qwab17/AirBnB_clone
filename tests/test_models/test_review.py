#!/usr/bin/python3
"""
    Module that implements test cases for
    class Review

"""
import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """Class implementing Review test cases"""
    def test_instance(self):
        """Test instance of attributes"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_attributes(self):
        """Test class instance attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))

    def test_str_representation(self):
        """Test the __str__ method on Review"""
        review = Review()
        expected_str = f"[Review] ({review.id}) {review.__dict__}"
        self.assertEqual(review.__str__(), expected_str)


if __name__ == "__main__":
    unittest.main()
