#!/usr/bin/python3
"""module tests doc"""
import unittest
from models.square import Square


class Test_Square(unittest.TestCase):
    """square tests"""
    def test_instance_method(self):
        """instances for square test doc"""
        sq = Square(1, 2, 3, 4)
        sq1 = Square(1, 2)
        sq2 = Square(1, 2, 3)
        with self.assertRaises(TypeError):
            sq_fail = Square("1")
        with self.assertRaises(TypeError):
            sq_fail = Square(1, "2")
        with self.assertRaises(TypeError):
            sq_fail = Square(1, 2, "3")
        with self.assertRaises(TypeError):
            sq_fail = Square('1', [2], 3, False)
        with self.assertRaises(ValueError):
            sq_fail = Square(-1, -2, 3.0, 4)
        with self.assertRaises(ValueError):
            sq_fail = Square(-1)
        with self.assertRaises(ValueError):
            sq_fail = Square(1, -2)
        with self.assertRaises(ValueError):
            sq_fail = Square(1, 2, -3)
        with self.assertRaises(ValueError):
            sq_fail = Square(0)

    def test_str(self):
        """str doc test"""
        sq = Square(2, 0, 0, 1)
        self.assertEqual(sq.__str__(), '[Square] (1) 0/0 - 2')

    def test_update(self):
        """update test doc"""
        sq = Square(4)
        sq.update(1, 2, 3)
        with self.assertRaises(ValueError):
            sq.update(0, -1)
        with self.assertRaises(TypeError):
            sq.update(2, 4, [])

    def test_area(self):
        """area test doc"""
        sq = Square(2)
        self.assertEqual(sq.area(), 4)

    def test_display(self):
        """display test doc"""
        import io
        import contextlib

        sq = Square(2, 0, 0, 1)
        with io.StringIO() as f:
            with contextlib.redirect_stdout(f):
                sq.display()
                printer = f.getvalue()
        self.assertEqual(printer, '##\n##\n')


if __name__ == '__main__':
    unittest.main()
