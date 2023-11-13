#!/usr/bin/python3
"""
mod def
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class method documentation
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        method documentation
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        method documentation
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        method documentation
        """

        self.width = value
        self.height = value

    def __str__(self):
        """str func"""
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return s.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        method documentation
        """

        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            valid_attributes = ['id', 'size', 'x', 'y']
            for key, value in kwargs.items():
                if key in valid_attributes:
                    if key == 'size':
                        for i in ["width", "height"]:
                            exec("self.{} = {}".format(i, value))
                            continue
                    exec("self.{} = {}".format(key, value))

    def to_dictionary(self):
        """
        method documentation
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
