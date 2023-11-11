#!/usr/bin/python3
""" mod def"""
from models.base import Base


class Rectangle(Base):
    """class def"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """ height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """ x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """validate method"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """area"""
        return self.width * self.height

    def display(self):
        """7-print rect"""
        s = '$\n' * self.y + \
            (' ' * self.x + '#' * self.width + '$\n') * self.height
        print(s, end='')

    def __str__(self):
        """12str"""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """ method"""
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if id is not None:
            self.id = id
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width

    def update(self, *args, **kwargs):
        """ instance attribute update"""
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """print x,y,id,height width"""
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width}
