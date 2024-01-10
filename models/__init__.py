#!/usr/bin/python3
"""
    Module to create unique file storage instance


"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
