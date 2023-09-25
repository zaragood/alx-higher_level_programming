#!/usr/bin/python3
"""importing the Base classs"""
from models.base import Base

"""creating a class 'Rectangle'"""


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor
         Initializing a class attribute with height and width
         x, y and id

        Args:
            @width (int): width of rectangle
            @Height (int): height of the rectangle
            @x (int)
            @y (int)
        """
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """getting the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the attribute width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getting the private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """sets the attribute of height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getting the private instance attribute x"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """sets the attribute of x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getting the private instance attribute y"""
        return (self.__height)

    @y.setter
    def y(self, y):
        """sets the attribute of y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        for _ in range(self.__y):
            print()
        for i in range(self.area()):
            if not (i % self.__width) and i != 0:
                print()
            if not (i % self.__width):
                for j in range(self.__x):
                    print(' ', end='')
            print('#', end='')
        print()

    def __str__(self):
        """method so that it returns a formated string"""
        a = str(self.id)
        b = str(self.__x)
        c = str(self.__y)
        d = str(self.__width)
        e = str(self.__height)
        r = "[Rectangle]"
        return r + "(" + a + ") " + b + '/' + c + ' - ' + d + '/' + e

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        arguments = ['id', 'width', 'height', 'x', 'y']

        if args:
            for i, arg_name in enumerate(arguments):
                if i < len(args):
                    setattr(self, arg_name, args[i])
        else:
            for key, value in kwargs.items():
                if key in arguments:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of Rect"""
        return {
                "x": self.__x,
                "y": self.__y,
                "id": self.id,
                "height": self.__height,
                "width": self.__width
                }
