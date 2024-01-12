#!/usr/bin/python3
"""
    Module with class City that inherits from
    base class BaseModel

"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City that instantiates city objects"""
    state_id = ""   # state.id
    name = ""
