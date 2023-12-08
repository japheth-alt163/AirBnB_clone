#!/usr/bin/python3
"""
Unittests for console
"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from console import HBNBCommand
from io import StringIO
import sys

class TestConsole(unittest.TestCase):
    def setUp(self):
        """
        Set up test environment
        """
        self.console_output = StringIO()
        sys.stdout = self.console_output

    def tearDown(self):
        """
        Clean up test environment
        """
        sys.stdout = sys.__stdout__
        del self.console_output

    def test_create(self):
        """
        Test create command
        """
        HBNBCommand().onecmd("create User")
        captured_output = self.console_output.getvalue().strip()
        self.assertTrue(len(captured_output) == 36)

    def test_show(self):
        """
        Test show command
        """
        HBNBCommand().onecmd("create User")
        obj_id = self.console_output.getvalue().strip()
        self.console_output = StringIO()
        HBNBCommand().onecmd("show User {}".format(obj_id))
        captured_output = self.console_output.getvalue().strip()
        self.assertTrue(obj_id in captured_output)

    def test_destroy(self):
        """
        Test destroy command
        """
        HBNBCommand().onecmd("create User")
        obj_id = self.console_output.getvalue().strip()
        self.console_output = StringIO()
        HBNBCommand().onecmd("destroy User {}".format(obj_id))
        objects_path = "file.json"
        with open(objects_path, 'r') as file:
            content = file.read()
            self.assertFalse(obj_id in content)

    def test_all(self):
        """
        Test all command
        """
        HBNBCommand().onecmd("create User")
        obj_id = self.console_output.getvalue().strip()
        self.console_output = StringIO()
        HBNBCommand().onecmd("all User")
        captured_output = self.console_output.getvalue().strip()
        self.assertTrue(obj_id in captured_output)

    def test_update(self):
        """
        Test update command
        """
        HBNBCommand().onecmd("create User")
        obj_id = self.console_output.getvalue().strip()
        self.console_output = StringIO()
        HBNBCommand().onecmd("update User {} first_name 'John'".format(obj_id))
        objects_path = "file.json"
        with open(objects_path, 'r') as file:
            content = file.read()
            self.assertTrue('"first_name": "John"' in content)

if __name__ == '__main__':
    unittest.main()
