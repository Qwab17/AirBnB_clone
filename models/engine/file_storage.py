#!/usr/bin/python3
"""
    Module with class FileStorage that implements
    data persistence by writing to json file

"""
import json


class FileStorage():
    """Class to serialize and deserialize to/from json file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method to return instance dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Method to add key/value pair to dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Method to serialize dictionary to JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            jn_dct = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(jn_dct, f)

    def reload(self):
        """Method to deserialize JSON file to dictionary"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        try:
            with open(FileStorage.__file_path, "r") as f:
                jsn_dct = json.load(f)
                for k, v in jsn_dct.items():
                    cls_name = v["__class__"]
                    del v["__class__"]
                    FileStorage.__objects[k] = eval(cls_name)(**v)
        except FileNotFoundError:
            pass
