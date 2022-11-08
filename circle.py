"""
REFRENCES:

Bresenham complete circle algorithm [1]
Original Code was modified, the original code can be found here: https://www.daniweb.com/programming/software-development/threads/321181/python-bresenham-circle-arc-algorithm 

"""
from PIL import Image, ImageDraw
import numpy as np

class Circle:
    def __init__(self, radius, img_arr, height, width, cx, cy) -> None:
        self.radius = radius # This stands for the amount of layers.
        self.data = np.zeros((height, width)) # Create an empty 2d array with same dimensions as the image:
        self.cx = cx # Circle Center X.
        self.cy = cy # Circle Center Y.
        
        pass

    def create_circle_outline(self, radius):
        """ [1] """

        "Bresenham complete circle algorithm in Python"
        # init vars
        switch = 3 - (2 * radius)
        x = 0
        y = self.radius
        # first quarter/octant starts clockwise at 12 o'clock
        while x <= y:
            # first quarter first octant
            self.data[self.cx + x, self.cy - y] = (255, 0, 0)
            # first quarter 2nd octant
            self.data[self.cy + y, self.cx -x ] = (255, 0, 0)
            # second quarter 3rd octant
            self.data[self.cy + y, self.cx + x] = (255, 0, 0)
            # second quarter 4.octant
            self.data[self.cx + x, self.cy + y] = (255, 0, 0)
            # third quarter 5.octant
            self.data[self.cx - x, self.cy + y] = (255, 0, 0)        
            # third quarter 6.octant
            self.data[self.cy - y, self.cx + x] = (255, 0, 0)
            # fourth quarter 7.octantb
            self.data[self.cy - y,self.cx - x] = (255, 0, 0)
            # fourth quarter 8.octant
            self.data[self.cx - x, self.cy - y] = (255, 0, 0)

            if switch < 0:
                switch = switch + (4 * x) + 6
            else:
                switch = switch + (4 * (x - y)) + 10
                y = y - 1
            x = x + 1
    

    def circleBres(self):
        x = 0
        y = self.radius
        d = 3 - (2 * self.radius)
        
        # DRAW:
        self.draw(self.cx, self.cy, x, y)
        while y >= x:
            # For each pixel, 8 will be drawn:
            x += 1

            # Check for desicion parameter:
            if d > 0:
                y -= 1
                d = d + 4 * (x - y) + 10
            else:
                d = d + 4 * x + 6

            # Place the pixel:
            self.draw(self.cx, self.cy, x, y)
            
    def draw(self, cx, cy, x, y):
        self.data[cx + x, cy + y] = [255, 0, 0]
        self.data[cx - x, cy + y] = [255, 0, 0]
        self.data[cx + x, cy - y] = [255, 0, 0]
        self.data[cx - x, cy - y] = [255, 0, 0]
        self.data[cx + y, cy + x] = [255, 0, 0]
        self.data[cx - y, cy + x] = [255, 0, 0]
        self.data[cx + y, cy - x] = [255, 0, 0]
        self.data[cx - y, cy - x] = [255, 0, 0]           

    
    def create_circle(self):
        for i in range(1, self.radius):
            self.create_circle_outline(i)

        return self.data
    
    