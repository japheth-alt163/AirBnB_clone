#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def setUp(self):
        """Set up method to prepare test environment"""
        self.city = City()

    def tearDown(self):
        """Tear down method to clean up test environment"""
        del self.city

    def test_state_id_attribute(self):
        """Test the existence and type of state_id attribute"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertIsInstance(self.city.state_id, str)
        self.assertEqual(self.city.state_id, "")

    def test_name_attribute(self):
        """Test the existence and type of name attribute"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        """Test if City class inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_init_method(self):
        """Test the __init__ method"""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict() method"""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('__class__', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(datetime.strptime(city_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertIsInstance(datetime.strptime(city_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertEqual(city_dict['state_id'], "")
        self.assertEqual(city_dict['name'], "")


if __name__ == '__main__':
    unittest.main()
