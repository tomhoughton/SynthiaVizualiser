from gradient_cls import Gradient
from PIL import Image, ImageDraw
from animate import Animate

class Layer:
    def __init__(self, gradient: Gradient, draw_points, type, size) -> None:
        self.gradient = gradient
        self.draw_points = draw_points # If draw points = None then is the background.
        self.type = type
        self.size = size
        
        self.frame = Image.new('RGB', (300, 300), (0, 0, 0))
        self.draw = ImageDraw.Draw(self.frame)

        # Create animation object:
        self.animate = Animate(anim_type="expo")

    def draw_layer(self, anim_value):

        frame_return = None

        if self.type == 'circle':
            frame_return = self.draw_circle(anim_value=anim_value)
        elif self.type == 'back':
            frame_return = self.draw_background(anim_value=anim_value)

        return frame_return

    def draw_circle(self, anim_value):
        #print('Draw Circle')

        animated_RGB = self.animate.anim(x=anim_value)

        for r, circle in enumerate(self.draw_points):
            # Calculate the color of the circles ring:
            color = self.gradient.calculate_color(x_coord=r, y_coord=0)
            color[1] = animated_RGB # Set the G value to be animated.
            color[2] = animated_RGB # Set the B value to be animated.

            for p in circle:
                self.draw.point((int(self.size/2+p[0]), int(self.size/2+p[1])), tuple(color))

        # self.frame.show()

        return self.frame
        

    def draw_background(self, anim_value) -> Image:
        #print('back')

        # Calculate the animated color value:
        animated_RGB =  self.animate.anim(x=anim_value)

        for y in range(0, self.size):
            for x in range(0, self.size):
                color = self.gradient.calculate_color(x_coord=y, y_coord=0)
                color[1] = animated_RGB # Set the G value to be animated.

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