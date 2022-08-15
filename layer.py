
class Layer:
    def __init__(self, gradient, scaled_data, draw_points, width, hieght) -> None:
        self.gradient = gradient
        self.draw_points = draw_points # If draw points = None then is the background.
        self.scaled_data = scaled_data
        self.isBackground = None
        self.frame = None # ImageFrame
        self.draw = None # ImageDraw
    
    

    