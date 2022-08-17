from gradient import Gradient
from PIL import Image, ImageDraw

class Layer:
    def __init__(self, gradient: Gradient, draw_points, type, size) -> None:
        self.gradient = gradient
        self.draw_points = draw_points # If draw points = None then is the background.
        self.type = type
        self.size = size
        
        self.frame = Image.new('RGB', (300, 300), (0, 0, 0))
        self.draw = ImageDraw.Draw(self.frame)

    def draw_layer(self, anim_value):

        frame_return = None

        if self.type == 'circle':
            frame_return = self.draw_circle()
        elif self.type == 'back':
            frame_return = self.draw_background()

        return frame_return

    def draw_circle(self):
        #print('Draw Circle')

        for r, circle in enumerate(self.draw_points):
            # Calculate the color of the circles ring:
            color = self.gradient.calculate_color(x_coord=r, y_coord=0)

            for p in circle:
                self.draw.point((int(self.size/2+p[0]), int(self.size/2+p[1])), tuple(color))

        # self.frame.show()

        return self.frame
        

    def draw_background(self) -> Image:
        #print('back')
        for y in range(0, self.size):
            for x in range(0, self.size):
                color = self.gradient.calculate_color(x_coord=y, y_coord=0)
                self.frame.putpixel((x, y), tuple(color))
        
        # self.frame.show()
        return self.frame


    def create_frame(self):
        """Create a new Image Frame and Draw.

        Returns:
            frame: image frame
            draw: image draw
        """
        frame = Image.new('RGB', (300, 300), (0, 0, 0))
        draw = ImageDraw.Draw(frame)

        return frame, draw