#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def setUp(self):
        """Set up method to prepare test environment"""
        self.state = State()

    def tearDown(self):
        """Tear down method to clean up test environment"""
        del self.state

    def test_name_attribute(self):
        """Test the existence and type of name attribute"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertIsInstance(self.state.name, str)
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Test if State class inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_init_method(self):
        """Test the __init__ method"""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict() method"""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(datetime.strptime(state_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertIsInstance(datetime.strptime(state_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertEqual(state_dict['name'], "")


if __name__ == '__main__':
    unittest.main()
