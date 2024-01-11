#!/usr/bin/python3
"""
    Module with class User that inherits from
    BaseModel class

"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from base class, BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
