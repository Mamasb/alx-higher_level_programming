#!/usr/bin/python3
"""Documentation for a square class"""

class Square:
    """Represents a square class of quadrilateral wityh four equal sides

    Attributes:
       __size (int): size of a side of the square
       """
    def __init__(self, size=0):
        """Initializesd a new square

           Args:
               size (int): size of a side of a squarte

           Returns:
              None

           Raises:
                 ValueError: when thge value passed is lessthan 0
                 TYypeError:when the value passed is not an iunteger
           """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        else:
           self.__size = size



