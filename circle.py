"""
REFRENCES:

Bresenham complete circle algorithm [1]
Original Code was modified, the original code can be found here: https://www.daniweb.com/programming/software-development/threads/321181/python-bresenham-circle-arc-algorithm 

"""
from PIL import ImageDraw

class Circle:
    def __init__(self, radius, img) -> None:
        self.radius = radius # This stands for the amount of layers.
        self.draw = ImageDraw.Draw(img)
        self.draw.point()
        pass

    def create_circle_outline(self):
        """ [1] """

        "Bresenham complete circle algorithm in Python"
        # init vars
        switch = 3 - (2 * self.radius)
        points = set()
        x = 0
        y = self.radius
        # first quarter/octant starts clockwise at 12 o'clock
        while x <= y:
            # first quarter first octant
            points.add((x,-y))
            # first quarter 2nd octant
            points.add((y,-x))
            # second quarter 3rd octant
            points.add((y,x))
            # second quarter 4.octant
            points.add((x,y))
            # third quarter 5.octant
            points.add((-x,y))        
            # third quarter 6.octant
            points.add((-y,x))
            # fourth quarter 7.octant
            points.add((-y,-x))
            # fourth quarter 8.octant
            points.add((-x,-y))
            if switch < 0:
                switch = switch + (4 * x) + 6
            else:
                switch = switch + (4 * (x - y)) + 10
                y = y - 1
            x = x + 1
        return points

