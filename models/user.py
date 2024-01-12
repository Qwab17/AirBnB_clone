#!/usr/bin/python3
"""
    Module with class User that inherits from
    base class BaseModel

"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel as base class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
