# circle class
from math import pi
class Circle:
    def __init__(self, radius: float):
        """
        Initialize a circle object with the given radius.

        Parameters:
        radius( float): The radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """
        calculate and return the area of the circle.

        return:
        float: the area of the circle.
        """
        return pi * (self.radius ** 2)

    def circumference(self) -> float:
        """
        Calculate and return the circumference of the circle.

        Returns:
            float: the circumference of the circle.
        """
        return 2 * pi * self.radius

circle = Circle(5.0)
print(circle.area())
print(circle.circumference())