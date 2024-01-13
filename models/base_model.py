#!/usr/bin/python3
"""
    Module to implement a class BaseModel that defines
    attributes/methods for other classes

"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """Class that defines attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Method to initialize instance attributes"""
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
            storage.new(self)

    def __str__(self):
        """Method that prints formatted output"""
        cls_name = self.__class__.__name__
        return f"[{cls_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Method to update time an instance is updated"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Method that returns dictionary representation of instance"""
        instance_dct = self.__dict__.copy()
        cls_name = self.__class__.__name__
        instance_dct["__class__"] = cls_name
        instance_dct["created_at"] = self.created_at.isoformat()
        instance_dct["updated_at"] = self.updated_at.isoformat()
        return instance_dct
