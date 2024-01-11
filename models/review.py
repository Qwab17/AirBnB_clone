#!/usr/bin/python3
"""
    Module with class Review that inherits from
    base class, BaseModel

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that inherits from BaseModel base class"""
    place_id = ""
    user_id = ""
    text = ""
