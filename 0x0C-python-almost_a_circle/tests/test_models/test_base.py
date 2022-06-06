#!/usr/bin/python3
""" Base unittest """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json
import pycodestyle
from os import path


class test_base(unittest.TestCase):
    """ Base test """
    def no_doc(item):
        """ Test decorators """
        decorator = "class" if inspect.isclass(item) else "function"
        item.__doc__ = ("This {} intentionally has no documentation".format(decorator))

    def test_base(self):
        """ Base """
        base0 = Base(1)
        self.assertEqual(base0.id, 1)
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)

    def test_to_json_string(self):
        """ To json string """
        sq = Square(1, 2, 3)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        rec = Rectangle(1, 2, 3, 4, 5)
        rec_dict = rec.to_dictionary()
        json_dict = Base.to_json_string([rec_dict])
        self.assertEqual(rec_dict, {'id': 5, 'width': 1,
                                    'height': 2, 'x': 3, 'y': 4})
        self.assertIs(type(rec_dict), dict)
        self.assertIs(type(json_dict), str)
        self.assertEqual(json.loads(json_dict), json.loads('[{"id": 5, '
                                                           '"width": 1, '
                                                           '"height": 2, '
                                                           '"x": 3, '
                                                           '"y": 4}]'))
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_dictionary(self):
        """ To dictionary """
        rec = Rectangle(1, 2, 3, 4)
        rec_dict = rec.to_dictionary()
        self.assertIs(type(rec_dict), dict)

    def test_create_rectangle(self):
        """ Creates rectangle"""
        rec = Rectangle(1, 2, 3, 4, 5)
        rec_dict = rec.to_dictionary()
        rec_new = Rectangle.create(**rec_dict)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(rec))
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(rec_new))
        self.assertIsNot(rec, rec_new)
        self.assertNotEqual(rec, rec_new)

    def test_create_square(self):
        """ Creates square """
        sq = Square(1, 2, 3, 4)
        sq_dict = sq.to_dictionary()
        sq_new = Square.create(**sq_dict)
        self.assertEqual("[Square] (4) 2/3 - 1", str(sq))
        self.assertEqual("[Square] (4) 2/3 - 1", str(sq_new))
        self.assertIsNot(sq, sq_new)
        self.assertNotEqual(sq, sq_new)

    def test_load_from_file(self):
        """ Loads from file """
        rec = Rectangle(1, 2)
        rec_json = Rectangle.save_to_file([rec])
        if not path.exists("Rectangle.json"):
            list_rec = Rectangle.load_from_file()
            self.assertEqual(list_rec, [])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual([rec.to_dictionary()], json.load(f))
        sq = Square(1)
        sq_json = Square.save_to_file([sq])
        if not path.exists("Square.json"):
            list_sq = Square.load_from_file()
            self.assertEqual(list_sq, [])
        with open("Square.json", 'r') as f:
            self.assertEqual([sq.to_dictionary()], json.load(f))

    def test_save_to_file(self):
        """ Saves to file """
        rec = Rectangle(1, 2)
        rec_json = Rectangle.save_to_file([rec])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual([rec.to_dictionary()], json.load(f))
        rec_none_json = Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertNotEqual([rec.to_dictionary()], json.load(f))
        rec_empty_json = Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as f:
            self.assertNotEqual([rec.to_dictionary()], json.load(f))
        sq = Square(1)
        sq_json = Square.save_to_file([sq])
        with open("Square.json", 'r') as f:
            self.assertEqual([sq.to_dictionary()], json.load(f))

    def test_from_json_string(self):
        """ From json string """
        base = Base.from_json_string(None)
        self.assertEqual(base, [])
        base_new = Base.from_json_string("[]")
        self.assertEqual(base_new, [])


class TestCodeFormat(unittest.TestCase):
    """ Code Format """
    def test_pycodestyle_conformance(self):
        """ Pycodestyle """
        pep = pycodestyle.StyleGuide(quiet=True)
        res = pep.check_files(['../../models/base.py'])
        self.assertEqual(res.total_errors, 1,\
         "You have code style errors.")


if __name__ == '__main__':
    unittest.main()
