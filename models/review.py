#!/usr/bin/python3
"""
    Module with class Review that inherits from
    base class BaseModel

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review to handle review instances"""
    place_id = ""   # place.id
    user_id = ""   # user.id
    text = ""
