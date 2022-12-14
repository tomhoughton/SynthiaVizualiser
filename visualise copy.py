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

class Visualise:
    def __init__(self, frame_amount, data, original_song) -> None:
        
        self.frame_amount = frame_amount # Stores the amount of frames needed.
        self.data = data # Stores the data of the sone (typically the scaled data).
        self.original_song = original_song # Store the original data just in case.
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
        """
        Each layer must have the following properties:
        - 2D Array of points.
        - A Gradient.

        """
        # Background Layer:
        # This layer will change colours based on audio.
        background_gradient = Gradient(
            startColor=(32, 121, 122), 
            endColor=(62, 198, 199), 
            isVerticle=False, 
            distance=255
        ) # NOTE: We are just animating a solid colour here in distance of 255.
        
        background_layer = Layer(
            gradient=background_gradient,
            draw_points=None,
            type='back',
            size=300
        )

        # Circle Layer:
        # This layer will display a circle, where the G value changes based on audio.
        # Create the gradient:
        circle_gradient = Gradient(startColor=(255, 0, 26), endColor=(205, 0, 255), isVerticle=True, distance=(60))
        circle_gradient.cacl_increase()
        circle_gradient.obtainM()

        # Create the frame:
        frame, draw = self.create_frame()
        frame_size = 300 

       
        return background_layer

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

            # Create a frame:
            frame = self.create_frame()
            frame_size = 300 # Holder: TODO: Make this define the size of the frame.
            


            """
            

            # Create a circle:
            c = Circle(radius=60)
            circles = c.get_circles()

            # Create a gradient:
            g = Gradient(startColor=(255, 0, 26), endColor=(205, 0, 255), isVerticle=True, distance=(60))
            g.cacl_increase()
            g.obtainM()

            # Animate a Value:
            # Obtain a new green value:
            green = self.animate_val(curr_RGB=x, new_x=data[sample_index])
            x = green # Re-instante the current RGB value.
            
            # Add to statistics values:
        
            self.smooth_colour_values.append(green)
            self.scaled_sample_value_at_color.append(data[i])

            # Loop through the circles to draw the gradient circle:
            for r, circle in enumerate(circles):

                # Calculate of value of the circles ring (layer).
                color = g.calculate_color(x_coord=r, y_coord=0)

                # Check to ensure the sample index isn't greater than total samples:
                if (sample_index > len(data)):
                    sample_index = len(data) - 1

                # Get G value:
                color[1] = int(green)
                t_color = tuple(color)

                # Index through the points in the circle to draw.
                for p in circle:
                    draw.point((int(frame_size/2+p[0]), int(frame_size/2+p[1])), t_color)

            """

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