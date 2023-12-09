#!/usr/bin/python3
"""
Module for BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class for storing common attributes/methods.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of BaseModel.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the public instance attribute
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
