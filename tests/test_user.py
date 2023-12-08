#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def setUp(self):
        """Set up method to prepare test environment"""
        self.user = User()

    def tearDown(self):
        """Tear down method to clean up test environment"""
        del self.user

    def test_email_attribute(self):
        """Test the existence and type of email attribute"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertIsInstance(self.user.email, str)

    def test_password_attribute(self):
        """Test the existence and type of password attribute"""
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertIsInstance(self.user.password, str)

    def test_first_name_attribute(self):
        """Test the existence and type of first_name attribute"""
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_attribute(self):
        """Test the existence and type of last_name attribute"""
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertIsInstance(self.user.last_name, str)

    def test_inheritance(self):
        """Test if User class inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_init_method(self):
        """Test the __init__ method"""
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_to_dict_method(self):
        """Test the to_dict() method"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(datetime.strptime(user_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertIsInstance(datetime.strptime(user_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)

    def test_kwargs_constructor(self):
        """Test the __init__ method with kwargs"""
        user_dict = self.user.to_dict()
        new_user = User(**user_dict)
        self.assertNotEqual(self.user, new_user)
        self.assertEqual(self.user.id, new_user.id)
        self.assertEqual(self.user.created_at, new_user.created_at)
        self.assertEqual(self.user.updated_at, new_user.updated_at)
        self.assertEqual(self.user.email, new_user.email)
        self.assertEqual(self.user.password, new_user.password)
        self.assertEqual(self.user.first_name, new_user.first_name)
        self.assertEqual(self.user.last_name, new_user.last_name)

    def test_kwargs_constructor_excluding_class_key(self):
        """Test the __init__ method with kwargs excluding __class__ key"""
        user_dict = self.user.to_dict()
        del user_dict['__class__']
        new_user = User(**user_dict)
        self.assertNotEqual(self.user, new_user)
        self.assertEqual(self.user.id, new_user.id)
        self.assertEqual(self.user.created_at, new_user.created_at)
        self.assertEqual(self.user.updated_at, new_user.updated_at)
        self.assertEqual(self.user.email, new_user.email)
        self.assertEqual(self.user.password, new_user.password)
        self.assertEqual(self.user.first_name, new_user.first_name)
        self.assertEqual(self.user.last_name, new_user.last_name)

if __name__ == '__main__':
    unittest.main()
