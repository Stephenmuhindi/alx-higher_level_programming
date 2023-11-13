#!/usr/bin/python3
""" mod def"""
import unittest
from turtle import Turtle, Screen
from json import dumps, loads
import os
from models.base import Base


class TestBase(unittest.TestCase):
    def test_A_nb_objects_private(self):
        '''Tests if nb_objects is a private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Tests Base() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_D_constructor(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_E_consecutive_ids(self):
        '''Tests consecutive ids.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_G_custom_id_int(self):
        '''Tests custom int id.'''
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_custom_id_str(self):
        '''Tests custom int id.'''
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_G_id_keyword(self):
        '''Tests id passed as a keyword argument.'''
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)

    def test_H_to_json_string(self):
        '''Tests to_json_string() method.'''
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244, 'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))

        d = [{"foobarrooo": 989898}]
        self.assertEqual(Base.to_json_string(d), '[{"foobarrooo": 989898}]')

        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(d), '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]')

    def test_H_to_json_string(self):
        '''Tests to_json_string() method.'''
        # Case 1: Test with a list of dictionaries
        input_list = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        expected_output = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.to_json_string(input_list), expected_output)

        # Case 2: Test with an empty list
        self.assertEqual(Base.to_json_string([]), "[]")

        # Case 3: Test with None
        self.assertEqual(Base.to_json_string(None), "[]")

        # Add more test cases as needed

    def test_I_save_to_file(self):
        '''Tests save_to_file() method.'''
        # Case 1: Test saving to a file with a list of objects
        r1 = Base()
        r2 = Base()
        Base.save_to_file([r1, r2])

        # Check if the file "Base.json" is created
        self.assertTrue(os.path.exists("Base.json"))

        # Case 2: Test saving to a file with None
        Base.save_to_file(None)
        self.assertTrue(os.path.exists("Base.json"))

        # Case 3: Test saving to a file with an empty list
        Base.save_to_file([])
        self.assertTrue(os.path.exists("Base.json"))

        # Add more test cases as needed

    def test_J_create(self):
        '''Tests create() method.'''
        # Case 1: Test creating an object from a dictionary
        input_dict = {'id': 1}
        created_object = Base.create(**input_dict)
        self.assertIsInstance(created_object, Base)
        self.assertEqual(created_object.id, input_dict['id'])

        # Add more test cases as needed

    def test_K_load_from_file(self):
        '''Tests load_from_file() method.'''
        # Case 1: Test loading from a file with existing data
        r1 = Base()
        r2 = Base()
        Base.save_to_file([r1, r2])
        loaded_objects = Base.load_from_file()
        self.assertEqual(len(loaded_objects), 2)
        self.assertIsInstance(loaded_objects[0], Base)
        self.assertIsInstance(loaded_objects[1], Base)

        # Case 2: Test loading from a file with no data
        Base.save_to_file(None)
        loaded_objects = Base.load_from_file()
        self.assertEqual(loaded_objects, [])

        # Case 3: Test loading from a non-existent file
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        loaded_objects = Base.load_from_file()
        self.assertEqual(loaded_objects, [])
def test_L_draw(self):
        '''Tests draw() method.'''
        # Case 1: Test drawing rectangles and squares
        r1 = Base()
        r2 = Base()
        s1 = Base()
        s2 = Base()
        list_rectangles = [r1, r2]
        list_squares = [s1, s2]

        screen = Screen()
        screen.bgcolor("black")

        pen = Turtle()
        pen.speed(0)
        pen.color("white")

        Base.draw(list_rectangles, list_squares)

        # The drawing will be displayed visually, you can manually check

        screen.bye()


if __name__ == "__main__":
    unittest.main()

