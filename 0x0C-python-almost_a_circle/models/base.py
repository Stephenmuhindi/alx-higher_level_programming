#!/usr/bin/python3
""" mod def"""
from json import dumps, loads
import csv
import os


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

    @classmethod
    def load_from_file(cls):
        """19"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in list_dicts]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to CSV file"""
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height,
                                     obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize CSV file to list of objects"""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {'id': int(row[0]), 'width': int(row[1]),
                                      'height': int(row[2]),
                                      'x': int(row[3]), 'y': int(row[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {'id': int(row[0]), 'size': int(row[1]),
                                      'x': int(row[2]), 'y': int(row[3])}
                    instances.append(cls.create(**dictionary))
                return instances
        except FileNotFoundError:
            return []
