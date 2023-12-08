#!/usr/bin/python3
"""
Module for User class.
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class for storing user information.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of User.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
