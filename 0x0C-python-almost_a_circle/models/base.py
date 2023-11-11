#!/usr/bin/python3
""" mod def"""
from json import dumps, loads
import csv


class Base:
    """zero"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to instance"""
        if cls.__name__ == "Rectangle":
            holder = cls(1, 1)
        if cls.__name__ == "Square":
            holder = cls(1)
        holder.update(**dictionary)
        return holder

    @classmethod
    def load_from_file(cls):
        """18"""
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as file:
            stuff = cls.from_json_string(file.read())
        return [cls.create(**index) for index in stuff]
