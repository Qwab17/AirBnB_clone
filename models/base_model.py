#!/usr/bin/python
"""
    Module with class Base that defines common
    attributes/methods for other classes

"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class that defines attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Method that initializes attributes"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k in ("created_at, updated_at"):
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Method to format output for print"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates public instance attribute's current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all k/v pairs"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
