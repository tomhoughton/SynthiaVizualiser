""" 
What will this do?
- Create and store frames.
- Export the audio.
"""

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

class Visualise:
    def __init__(self, frame_amount, data) -> None:
        
        self.frame_amount = frame_amount # Stores the amount of frames needed.
        self.data = data # Stores the data of the sone (typically the scaled data).
        #self.original_song = original_song # Store the original data just in case.
        self.export_path = os.path.join('video') # The path to export the video to.
        self.frames = [] # The frame addresses.

        # Statistics:
        # Smooth colour value.
        # self.stats = Stats()
        self.smooth_colour_values = []
        self.scaled_sample_value_at_color = []

        pass

    def write_video(self) -> bool:
        """Create and save the new video.

        Returns:
            bool: just to see if it made it or not.
        """

        if len(self.frames) > 0:                
            # Store opened frames:
            new_frames = []

            for filename in self.frames:

                # Open frame:
                img = cv2.imread(os.path.join(self.export_path, filename))
                height, width, layers = img.shape # Get the dimensions.
                size = (width, height) # Gather the size.
                new_frames.append(img) # Append the image to the array.

            # Create a vido out object.
            out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 60, size)

            # Write frames to out:
            for i in range(len(new_frames)):
                out.write(new_frames[i])

            # Release the video:
            out.release()

            return self.smooth_colour_values, self.scaled_sample_value_at_color
        else:
            print('Must create new frames first')
            return False

    def create_layers(self, data):
        """ There are type main types of layer
                - Background layer -> Just a backgground.
                - Frequency Point layer -> A circle.
        """
        
        """ Background layer"""
        back_g = Gradient(
            startColor=(0, 187, 217),
            endColor=(205, 140, 199),
            isVerticle=True,
            distance=300
        ) # Create the gradient.

        # Create the gradient's necesarry values TODO: Include these in the constructor.
        back_g.cacl_increase()
        back_g.obtainM()
        
        # Create the background layer:
        background_layer = Layer(
            gradient=back_g,
            draw_points=None,
            type='back',
            size=300 
        )

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

        """ Return the data """
        layers = []
        layers.append(background_layer)
        layers.append(circle_layer)
       
        return layers

    def create_frames(self,frames, data):
        """This function creates all individual frames for the visuals and stores in the video directory.

        Args:
            frames (int): the amount of frames.
            data ([int]): The audio data

        Returns:
            bool: confimation
        """

        sample_index = 0 # Index to access per frame.
        x = 0

        # Layers List:
        layers_amount = 2
        layers = self.create_layers(data=None)

        # Create and save the necesarry frames:
        for i in range(0, frames): 
            self.handle_progress(curr_frame=i)

            """ Create the parent frame """
            # Create a frame:
            frame = Image.new('RGB', (300, 300), (0, 0, 0))
            draw = ImageDraw.Draw(frame)
            frame_size = 300 # Holder: TODO: Make this define the size of the frame.
            
            """ Draw the points on the frame with the appropriate colours"""
            # NOTE: This is where the animation and transformations should occur through passing in a value.
            # Render the frames:
            # TODO: Try and improve the speed of this.

            #NOTE
            """
            What I'm thinking is, instead of having draw functions in the layer,
            It would make more sense for the drawing 'rendering' of the layers to be in the same place 
            as wehere everything else renders.  

            This means that a layer must store things such as points, types, colours and how
            it changes over time.

            What this also means, is that each layers pixel should be done at the same time.

            Even potentially blending each colour at the same time.

            It is late when writing this comment, so who knows.

            However, this could be a direction to look at when improving the speed of the algorithm,
            
            """

            # At each frame, the colours (pixels) are decided here,
            # So we need to pass the anim value as that new value in range of 0 - 255
            rendered_layers = []
            for layer in layers:
                render = layer.draw_layer(anim_value=data[sample_index])
                rendered_layers.append(render)

            """Combine all the layers into one"""
            for y in range(0, frame.height):
                for x in range(0, frame.width):
                    
                    """This is where my not so good method of colour blending comes into play"""
                    # NOTE: Should probably make a function to blend the colours.
                    # For each pixel we need to get the pixel of each layer and store in a list:
                    pixels = []
                    for layer in rendered_layers:
                        pixels.append(layer.getpixel((x, y)))

                    r_total = 0
                    g_total = 0
                    b_total = 0

                    # Then we ned to toal this all up:
                    for pixel in pixels:
                        r_total = (r_total + pixel[0])
                        g_total = (g_total + pixel[1])
                        b_total = (b_total + pixel[2])

                    final_pixel = (r_total, g_total, b_total)
                    frame.putpixel((x, y), final_pixel)

            """ Save the Frame """
            # Save the frame and append to the list: 
            name = str(i) + '.jpg'
            frame.save(os.path.join(self.export_path, name))
            self.frames.append(name)

            # Increase the sample index:
            if ((sample_index + 375) > len(data)):
                sample_index = len(data) - 1
            else:
                sample_index += 375

        return True
            
    def animate_val(self, curr_RGB, new_x):
        """Logic to change an R/G/B value over time.

        Args:
            curr_RGB (int): _description_
            new_x (int): the sample value.

        Returns:
            int: returned R/G/B value. 
        """


        new_RGB = self.exponential_RGB(x=new_x)

        if (new_RGB > curr_RGB):
            return new_RGB
        else: 
            return curr_RGB - 1


    def exponential_RGB(self, x):
        """Exponential function to determine value in range of y=0-255.

        Args:
            x (int): x axis (-124 - 0).

        Returns:
            int: y axis (0-255)
        """

        """ 
        TODO: Improve this graph and function to make the curve steeper.
        """

        h = 58.1392623
        c = 0
        b = 1.1
        #return (b**(-x + h)) + c # Inverse/decay
        return (b**(x + h)) + c

    def create_frame(self):
        """Create a new Image Frame and Draw.

        Returns:
            frame: image frame
            draw: image draw
        """
        frame = Image.new('RGB', (300, 300), (0, 0, 0))
        draw = ImageDraw.Draw(frame)

        return frame, draw
   
    def handle_progress(self, curr_frame):
        """Handles render progress.

        Args:
            curr_frame (int): frame index
        """
        self.clear_console()
        print('Curr Frame: ', curr_frame, ' | ', str((curr_frame / self.frame_amount) * 100), '%')

    def clear_console(self):
        """Clears the console.

        Returns:
            None: nothing
        """
        clear = lambda: os.system('clear')
        clear()
        return None