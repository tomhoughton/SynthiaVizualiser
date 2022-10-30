"""
REFRENCES:

Bresenham complete circle algorithm [1]
Original Code was modified, the original code can be found here: https://www.daniweb.com/programming/software-development/threads/321181/python-bresenham-circle-arc-algorithm 

"""

import PIL.Image, PIL.ImageDraw

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
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
    
    def get_circle(self, c_width, c_height):
        size = 100
        radius = 40
        # circle_graph = PIL.Image.new("RGB", (size, size), (0,0,0))
        # draw = PIL.ImageDraw.Draw(circle_graph)
        p = self.create_circle_outline()
        return p

    def get_circles(self):
        circles = []
        for r in range(0, self.radius):
            new_c = Circle(r)
            circle_points = new_c.get_circle(50, 50)
            circles.append(circle_points)

        return circles
         