#!/usr/bin/python3
"""
    Module to implement data persistence by
    creating a unique filestorage from
    FileStorage class
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
