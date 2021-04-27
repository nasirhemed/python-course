import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

# Create a class Circle
# Each circle has a radius and the position of the center
# Write two methods to calculate area and circumference
# use math.Pi to get the value of pi

class Circle:
    pass