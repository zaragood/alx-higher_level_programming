#!/usr/bin/python3
""" This module creates a class: Base """
import json


class Base:
    """definning a Base class with private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """definning a class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the json representation of a python dic"""
        if list_dictionaries is None:
            return "[]"
        return  json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string repres of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        """convert the list_objs to a list of dictionaries"""
        list_dicts = [obj.dictionary() for onj in list_objs]

        """convert the list of dict to a json string"""
        json_string = cls.to_json_string(list_dicts)

        """write the string to a file.json"""
        with open(filename, "w", encoding='utf-8') as fp:
            fp.write(json_string)
