from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest

class TestBase(unittest.TestCase):
    def setUp(self):
        print("setUp")
    
    def tearDown(self):
        Base._Base__nb_objects = 0
        print("TearDown")

    def test_constructor_with_id(self):
        """test the constructor when an id is provided"""
        obj = Base(12)
        self.assertEqual(obj.id, 12)

    def test_constructor_without_id(self):
        """Test the constructor when id is not passed"""
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

class TestRectangle(unittest.TestCase):
    def setUp(self):
         print("setUp")

    def tearDown(self):
        Rectangle._Base__nb_objects = 0
        print("TearDown")

    def test_rect_constructor_with_id(self):
        """test the constructor when an id is provided"""
        rect = Rectangle(10, 2, 0, 2, 12)
        self.assertEqual(rect.id, 12)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 2)

    def test_rect_constructor_without_id(self):
        """Test the constructor when id is not passed"""
        rect1 = Rectangle(10, 2)
        rect2 = Rectangle(2, 10)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect2.id, 2)
        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect2.width, 2)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect2.height, 10)

    def test_type(self):
        """check if inputs are integers"""
        rect = Rectangle(10, "2")
        rect2 = Rectangle("10", 2)
        if isinstance(rect2.width, int):
            raise AssertionError("width must not be an integer")
        if isinstance(rect.height, int):
            raise AssertionError("height must not be an integer")

   """ def test_less_than_0(self):
        checking if the input is less than 0
        rect1 = Rectangle(10, 3)
        rect1.width = -5
        rect2 = Rectangle(10, 4)
        rect2.height = -2
        if rect2.height < 0:
            raise AssertionError("height must be > 0")
        if rect1.width < 0:
            raise AssertionError("width must be > 0")
    """
