#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import os
import json
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up method to prepare test environment"""
        try:
            os.rename('file.json', 'tempfile.json')
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Tear down method to clean up test environment"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass
        try:
            os.rename('tempfile.json', 'file.json')
        except FileNotFoundError:
            pass

    def test_file_path(self):
        """Test the default file path"""
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, 'file.json')

    def test_objects(self):
        """Test the default objects dictionary"""
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__objects, {})

    def test_all(self):
        """Test the all() method"""
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertEqual(type(obj_dict), dict)
        self.assertIs(obj_dict, storage._FileStorage__objects)

    def test_new(self):
        """Test the new() method"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        obj_dict = storage.all()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, obj_dict)

    def test_save(self):
        """Test the save() method"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        with open('file.json', 'r') as file:
            data = json.load(file)
            self.assertIn(key, data)

    def test_reload(self):
        """Test the reload() method"""
        storage1 = FileStorage()
        obj = BaseModel()
        storage1.new(obj)
        storage1.save()

        storage2 = FileStorage()
        storage2.reload()
        obj_dict = storage2.all()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, obj_dict)

    def test_reload_nonexistent_file(self):
        """Test reload when the file does not exist"""
        storage = FileStorage()
        storage.reload()
        self.assertEqual(storage.all(), {})

if __name__ == '__main__':
    unittest.main()
