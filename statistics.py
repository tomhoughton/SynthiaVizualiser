import matplotlib
import matplotlib.pyplot as plt

class Stats:
    def __init__(self) -> None:
        self.smooth_colour_values = []
        self.scaled_sample_value_at_color = []


    def add_smooth_value(self, val):
        self.smooth_colour_values.append(val)

    def add_sample_value(self, val):
        self.scaled_sample_value_at_color.append(val)