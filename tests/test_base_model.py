#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up method to prepare test environment"""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down method to clean up test environment"""
        del self.model

    def test_id_type(self):
        """Test the type of id attribute"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at_type(self):
        """Test the type of created_at attribute"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """Test the type of updated_at attribute"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """Test the save() method"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_str(self):
        """Test the str() method"""
        string = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), string)

    def test_to_dict(self):
        """Test the to_dict() method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(datetime.strptime(model_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)
        self.assertIsInstance(datetime.strptime(model_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"), datetime)

    def test_kwargs_constructor(self):
        """Test the __init__ method with kwargs"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertNotEqual(self.model, new_model)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)

    def test_kwargs_constructor_excluding_class_key(self):
        """Test the __init__ method with kwargs excluding __class__ key"""
        model_dict = self.model.to_dict()
        del model_dict['__class__']
        new_model = BaseModel(**model_dict)
        self.assertNotEqual(self.model, new_model)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)

if __name__ == '__main__':
    unittest.main()
