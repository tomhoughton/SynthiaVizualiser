"""
REFRENCES:

Bresenham complete circle algorithm [1]
Original Code was modified, the original code can be found here: https://www.daniweb.com/programming/software-development/threads/321181/python-bresenham-circle-arc-algorithm 

"""
from PIL import Image, ImageDraw

class Circle:
    def __init__(self, radius, img) -> None:
        self.radius = radius # This stands for the amount of layers.
        self.img = Image.new("RGB", (1000,  1000))
        self.draw = ImageDraw.Draw(self.img)
        self.points = set() # Create a set to store circle points
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
            self.draw.putpixel((x,-y), (255, 0, 0))
            # first quarter 2nd octant
            self.draw.putpixel((y,-x), (255, 0, 0))
            # second quarter 3rd octant
            self.draw.putpixel((y,x), (255, 0, 0))
            # second quarter 4.octant
            self.draw.putpixel((x,y), (255, 0, 0))
            # third quarter 5.octant
            self.draw.putpixel((-x,y), (255, 0, 0))        
            # third quarter 6.octant
            self.draw.putpixel((-y,x), (255, 0, 0))
            # fourth quarter 7.octant
            self.draw.putpixel((-y,-x), (255, 0, 0))
            # fourth quarter 8.octant
            self.draw.putpixel((-x,-y), (255, 0, 0))

            if switch < 0:
                switch = switch + (4 * x) + 6
            else:
                switch = switch + (4 * (x - y)) + 10
                y = y - 1
            x = x + 1

        
    
    def draw_circle(self):
        for i in range(1, self.radius):
            self.create_circle_outline(i)

        # We need a way to add points to the image draw.
        # What I really mean is, we need to find a way to add an image draw to an image.
        self.draw.show()
        return self.points
    
    