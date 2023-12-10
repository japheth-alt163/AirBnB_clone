#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def setUp(self):
        """Set up method to prepare test environment"""
        self.place = Place()

    def tearDown(self):
        """Tear down method to clean up test environment"""
        del self.place

    def test_city_id_attribute(self):
        """Test the existence and type of city_id attribute"""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(self.place.city_id, "")

    def test_user_id_attribute(self):
        """Test the existence and type of user_id attribute"""
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertIsInstance(self.place.user_id, str)
        self.assertEqual(self.place.user_id, "")

    def test_name_attribute(self):
        """Test the existence and type of name attribute"""
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertIsInstance(self.place.name, str)
        self.assertEqual(self.place.name, "")

    def test_description_attribute(self):
        """Test the existence and type of description attribute"""
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertIsInstance(self.place.description, str)
        self.assertEqual(self.place.description, "")


if __name__ == '__main__':
    unittest.main()
