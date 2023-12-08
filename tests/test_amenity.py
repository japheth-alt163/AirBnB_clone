#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def setUp(self):
        """Set up method to prepare test environment"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down method to clean up test environment"""
        del self.amenity

    def test_name_attribute(self):
        """Test the existence and type of name attribute"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertIsInstance(self.amenity.name, str)
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """Test if Amenity class inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_init_method(self):
        """Test the __init__ method"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict() method"""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('__class__', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(datetime.strptime(amenity_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertIsInstance(datetime.strptime(amenity_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertEqual(amenity_dict['name'], "")


if __name__ == '__main__':
    unittest.main()
