#!/usr/bin/python3
"""
    Module with class FileStorage that implements data
    persistence by writing to files

"""
import json


class FileStorage:
    """Class that serializesa and deserializes to/from json file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Method that returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Method to set given obj to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the dictionary (__objects) to JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            jn_dct = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(jn_dct, f)

    def reload(self):
        """Deserialises the JSON file to dictionary"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_dict = json.load(f)
                for k, v in json_dict.items():
                    cls_name = v["__class__"]
                    del v["__class__"]
                    FileStorage.__objects[k] = eval(cls_name)(**v)
        except FileNotFoundError:
            pass
