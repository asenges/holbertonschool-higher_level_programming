#!/usr/bin/python3
""" Module Base """
import json

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
