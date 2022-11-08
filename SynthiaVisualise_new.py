# Imports:
import os
from PIL import Image, ImageDraw
from gradient import Gradient # Import Gradient.
from circle import Circle
import random 
import numpy as np

def gradient_test():
    # Create a new Gradient Object:
    g = Gradient((190, 147, 197), (123, 198, 204), 1000)
    # NOTE: The distance will be the 'height: y' of the image.

    width, height = (1000, 1000) # Store the width and height of the image.

    img = Image.new("RGB", (width, height), (10, 10, 10))
    
    for y in range(0, height):
        for x in range(0, width):
            color = g.calculate_color_at_x(y)
            img.putpixel((x, y), color)

    img.show()


def circle_test():
    # Create an image:
    width, height = (1000, 1000) # Store the width and height of the image.
    img = Image.new("RGB", (1000, 1000), (0, 0, 255))
    img_arr = np.asarray(img)
    
    c = Circle(10, img_arr, height, width, width / 2, height / 2)
    c.circleBres()
    c_points = c.data

    for y in range(0, height):
        for x in range(0, width):
            img.putpixel((x, y), tuple(c_points[y, x]))

    img.show()

def circle_anim_test():
    
    # Firstly we need to create the animation logic:
    # Create an array of random numbers:
    fps = 60
    length = 60 # In seconds:
    test_data = np.zeros(fps * length)



def main():
    print('╭━━━╮╱╱╱╱╱╱╭╮╭╮╱╱╱╱╱╱╭╮╱╱╭╮╱╱╱╱╱╱╱╱╭╮')
    print('┃╭━╮┃╱╱╱╱╱╭╯╰┫┃╱╱╱╱╱╱┃╰╮╭╯┃╱╱╱╱╱╱╱╱┃┃')
    print('┃╰━━┳╮╱╭┳━╋╮╭┫╰━┳┳━━╮╰╮┃┃╭╋━━┳╮╭┳━━┫┃╭┳━━┳━━┳━╮')
    print('╰━━╮┃┃╱┃┃╭╮┫┃┃╭╮┣┫╭╮┃╱┃╰╯┣┫━━┫┃┃┃╭╮┃┃┣┫━━┫┃━┫╭╯')
    print('┃╰━╯┃╰━╯┃┃┃┃╰┫┃┃┃┃╭╮┃╱╰╮╭┫┣━━┃╰╯┃╭╮┃╰┫┣━━┃┃━┫┃')
    print('╰━━━┻━╮╭┻╯╰┻━┻╯╰┻┻╯╰╯╱╱╰╯╰┻━━┻━━┻╯╰┻━┻┻━━┻━━┻╯')
    print('╱╱╱╱╭━╯┃')
    print('╱╱╱╱╰━━╯')

    print('Please select whether you would like to go to tests or main: ')
    
    inp = input('1: main, 2: gradient test, 3: circle test, 4: circle animation test')

    if inp == '1':
        print('Main')
    elif inp == '2':
        gradient_test()
    elif inp == '3':
        circle_test()
    elif inp == '4':
        circle_anim_test()        


    print(' Choose a song to use: ')

    # Load the songs directory:
    music_dir = os.path.join('music')
    songs = os.listdir(music_dir)

    for i, song in enumerate(songs):
        print('[', i, ']: ', song)

    # Get some use input;
    usr = int(input('Select the song you would like to use'))
    
    
if __name__ == "__main__": 
    main()