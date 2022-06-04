#!/usr/bin/python3
"""rectangle test doc"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """rectangle class tests doc"""

    def test_instance_methods(self):
        """instances methods test doc"""
        rec = Rectangle(2, 3, 0, 0, 1)
        rec1 = Rectangle(1, 2)
        rec2 = Rectangle(1, 2, 3)
        rec3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rec.area(), 6)
        self.assertEqual(rec.__str__(), '[Rectangle] (1) 0/0 - 2/3')
        self.assertEqual(rec.to_dictionary(), {'id': 1,
                                               'width': 2,
                                               'height': 3,
                                               'x': 0,
                                               'y': 0})
        with self.assertRaises(ValueError):
            rec_fail = Rectangle(2, -3, 0, 0, 1)
            rec_new_fail = Rectangle(-1, 2)
            rec_another_fail = Rectangle(0, 2)
            rec_one_more_fail = Rectangle(1, 2, -3)
            rec_fails_yet = Rectangle(1, 2, 3, -4)
        with self.assertRaises(TypeError):
            rec_fail = Rectangle('Betty', 3, 0, 0, 1)
            rec_new_fail = Rectangle(None, 3, 0, 0, 1)
            rec_another_fail = Rectangle(2, 3, 0, 0, 1, 98)
            rec_one_more_fail = Rectangle(1, 2, 3, "4")

    def test_update(self):
        """update test doc"""
        rec = Rectangle(2, 3, 0, 0, 1)
        self.assertEqual(rec.to_dictionary(), {'id': 1,
                                               'width': 2,
                                               'height': 3,
                                               'x': 0,
                                               'y': 0})
        rec.update(98, 3, 1, 0, 0)
        self.assertEqual(rec.to_dictionary(), {'id': 98,
                                               'width': 3,
                                               'height': 1,
                                               'x': 0,
                                               'y': 0})
        rec_fail = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            rec_fail.update(1, '2', "Three", [4], {5})
        with self.assertRaises(TypeError):
            rec_fail = Rectangle(2.1, 3, 0, 0, 1)
        with self.assertRaises(TypeError):
            rec_fail = Rectangle(2, 3, float('inf'), 0, 1)
        with self.assertRaises(TypeError):
            rec_fail = Rectangle(2, 3, float('NaN'), 0, 1)
        with self.assertRaises(TypeError):
            rec_fail = Rectangle(2, True, 0, 0, 1)
        with self.assertRaises(ValueError):
            rec_fail = Rectangle(2, 0, 0, 0, 1)

    def test_arguments(self):
        """arguments test doc"""
        rec = Rectangle(2, 3, 0, 0, 1)
        self.assertEqual(rec.to_dictionary(), {'id': 1,
                                               'width': 2,
                                               'height': 3,
                                               'x': 0,
                                               'y': 0})
        rec.update(98, 3, 1, 0, 0)
        self.assertEqual(rec.to_dictionary(), {'id': 98,
                                               'width': 3,
                                               'height': 1,
                                               'x': 0,
                                               'y': 0})
        rec_fail = Rectangle(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            rec_fail.update(2, -3, 0, 0, 1)
        with self.assertRaises(TypeError):
            rec_fail.update(1, '98', 0, 0, 1)
        with self.assertRaises(ValueError):
            rec_fail.update(2, 0, 0, 0, 1)

    def test_area(self):
        """area test doc"""
        rec = Rectangle(2, 3)
        self.assertEqual(rec.area(), 6)

    def test_display(self):
        """display test doc"""
        import io
        import contextlib

        rec = Rectangle(2, 3, 0, 0, 1)
        with io.StringIO() as f:
            with contextlib.redirect_stdout(f):
                rec.display()
                instance = f.getvalue()
        self.assertEqual(instance, '##\n##\n##\n')

    def test_display_with_x_and_y(self):
        """display with x and y test doc"""
        import io
        import contextlib

        rec = Rectangle(2, 3, 1, 1, 1)
        with io.StringIO() as f:
            with contextlib.redirect_stdout(f):
                rec.display()
                instance = f.getvalue()
        self.assertEqual(instance, '\n ##\n ##\n ##\n')


if __name__ == '__main__':
    unittest.main()
