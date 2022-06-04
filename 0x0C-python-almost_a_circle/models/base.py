#!/usr/bin/python3
""" Module Base """
import json
from os import path


class Base:
    """ class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Object Builder  """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns json str """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves to a file """
        obj_list = []
        name = str(cls.__name__) + ".json"
        with open(name, 'w', encoding='utf8') as file:
            if list_objs is None:
                f.write(cls.to_json_string(obj_list))
            else:
                for obj in list_objs:
                    obj_list.append(cls.to_dictionary(obj))
                file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """ Retr json str to dict obj """
        obj_list = []
        if json_string is None:
            return obj_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attr """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        if cls.__name__ == "Square":
            obj = cls(1)
        if obj:
            obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ Loads from file """
        obj_list = []
        r_file = cls.__name__ + ".json"
        if path.isfile(r_file):
            with open(r_file, 'r') as file:
                for line in file:
                    obj = cls.from_json_string(line)
                    for i in obj:
                        obj_list.append(cls.create(**i))
        return obj_list
