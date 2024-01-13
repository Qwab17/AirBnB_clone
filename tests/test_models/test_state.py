#!/usr/bin/python3
"""
    Module that implements test cases for the
    State class

"""
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """Test State instance created"""
    def test_instance(self):
        """Test attribute instances"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertEqual(state.name, "")

    def test_attributes(self):
        """Verify instance attributes"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))

    def test_str_representation(self):
        """Test the __str__ method on State"""
        state = State()
        expected_str = f"[State] ({state.id}) {state.__dict__}"
        self.assertEqual(state.__str__(), expected_str)


if __name__ == "__main__":
    unittest.main()
