# Imports:
from layer import Layer
from gradient_cls import Gradient
from circle_old import Circle
import numpy as np 
from PIL import Image, ImageDraw

def main():
    
    # Image:
    img = Image.new('RGB', (300, 300), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Create a circle layer
    
    """ Circle Layer """
    # Create the gradient of the circle:
    circle_g = Gradient(
        startColor=(0, 255, 255),
        endColor=(0, 255, 0),
        isVerticle=True,
        distance=60
    )
    circle_g.cacl_increase()
    circle_g.obtainM()

    # Create a circle:
    c = Circle(radius=60)
    circles = np.array(c.get_circles())

    # Create the circle Layer:
    circle_layer = Layer(
        gradient=circle_g,
        draw_points=circles,
        type='circle',
        size=300
    )


    """ Render The Circle """
    circle_frame = circle_layer.draw_layer(anim_value=0.5)

    for y in range(0, img.height):
        for x in range(0, img.width):
            img.putpixel()



    



main()