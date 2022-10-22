
class Gradient:
    def __init__(self, start_color: tuple, end_color: tuple, distance: int):
        # Firstly we need to calculate m
        self.m = 255 / self.distance
        self.start_color = start_color
        self.end_color = self.end_color
        self.inc_dec_factor = self.calc_inc_dec()

    