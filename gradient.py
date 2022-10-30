
from ctypes.wintypes import DWORD


class Gradient:
    def __init__(self, start_color: tuple, end_color: tuple, distance: int):
        # Firstly we need to calculate m
        self.m = self.calculate_m(start_color, end_color, distance)

        print('M: ', self.m)

        self.start_color = start_color
        self.end_color = end_color

        # self.inc_dec_factor = self.calc_inc_dec()

    
    def calculate_m(self, start_color, end_color, distance) -> list:
        # RED: 
        m1 = (end_color[0] - start_color[0]) / distance
        m2 = (end_color[1] - start_color[1]) / distance
        m3 = (end_color[2] - start_color[2]) / distance

        return [m1, m2, m3] # Return gradient change for RGB.



    
    def calculate_color_at_x(self, x: int) -> tuple:
        
        # We need to return an RGB value for each distance:
        # y = mx + c: c = start color.

        r = int((self.m[0] * x) + self.start_color[0])
        g = int((self.m[1] * x) + self.start_color[1])
        b = int((self.m[2] * x) + self.start_color[2])

        return (r, g, b) 



    
    
