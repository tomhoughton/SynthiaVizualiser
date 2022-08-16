import os
from random import sample
from turtle import circle
import cv2
from PIL import Image, ImageDraw
from circle import Circle
from gradient import Gradient
from statistics import Stats
from layer import Layer
import numpy as np

def create_frame():
    """Create a new Image Frame and Draw.

    Returns:
        frame: image frame
        draw: image draw
    """
    frame = Image.new('RGB', (300, 300), (0, 0, 0))
    draw = ImageDraw.Draw(frame)

    return frame, draw

def create_layers(data):
    """
    Each layer must have the following properties:
    - 2D Array of points.
    - A Gradient.

    """
    # Background Layer:
    # This layer will change colours based on audio.
    g = Gradient(startColor=(0, 187, 217), endColor=(205, 140, 199), isVerticle=True, distance=255)
    g.cacl_increase()
    g.obtainM()

    background_layer = Layer(
        gradient=g,
        draw_points=None,
        type='back',
        size=300
    )

    # Circle Layer:
    # This layer will display a circle, where the G value changes based on audio.
    # Create the gradient:
    circle_gradient = Gradient(startColor=(0, 255, 255), endColor=(0, 255, 0), isVerticle=True, distance=(60))
    circle_gradient.cacl_increase()
    circle_gradient.obtainM()

    # Create a circle:
    c = Circle(radius=60)
    circles = np.array(c.get_circles())

    circle_layer = Layer(
        gradient=circle_gradient,
        draw_points=circles,
        type='circle',
        size=300
    )

    for r, circle in enumerate(circles):
        print('R: ', r)
        print(len(circle))

    # Create the frame:
    frame, draw = create_frame()
    frame_size = 300 

    # The layers need to be in an array:
    layers = []
    layers.append(background_layer)
    layers.append(circle_layer)

    return background_layer, circle_layer

def main():
    frame, draw = create_frame()

    # Create the layers:
    layers = create_layers(data=0)

    # Render the layers:
    rendered_layers = []
    for layer in layers:
        render = layer.draw_layer(anim_value=0)
        rendered_layers.append(render) 

    for y in range(0, frame.width):
        for x in range(0, frame.width):

            # For each pixel we need to get the pixel of each layer and store in a list:
            pixels = []
            for layer in rendered_layers:
                pixels.append(layer.getpixel((x, y)))
            
            r_total = 0
            g_total = 0
            b_total = 0

            # Then we need to total this all up:
            for pixel in pixels:
                r_total = (r_total + pixel[0])
                g_total = (g_total + pixel[1])
                b_total = (b_total + pixel[2])

            final_pixel = ((r_total), (g_total), (b_total))
            print(final_pixel)
            frame.putpixel((x, y), final_pixel)

    frame.show()



main()