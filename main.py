# So we basically need to get the data in and just change pixels.
# We also need to work out the amount of frames in the time frame
# And how to export audio with the video.
""" Imports """
import librosa
import librosa.display
import numpy as np
import os
from PIL import Image, ImageDraw
import cv2
import time

# My imports:
from gradient_cls import Gradient
from circle import Circle

"""

Global Stat variables.

"""

"""
Math Stuff
"""

def song_length_to_frames(y, sr, frames):
    
    # Get the duration as an int:
    duration = int(librosa.get_duration(y=y, sr=sr))
    rtn_frames = duration * frames # Multiply by frame rate.
    return rtn_frames

def get_linear_color(frame):

    # TODO: Get m dynamically.
    m = 0.018085106
    x = frame

    return x * m

def scale_f(unscaled, n_max, n_min, c_min, c_max):
    return ((n_max - n_min) * (unscaled - c_min) / (c_max - c_min)) + n_min

def scale_data(i_data, n_max, n_min, c_min, c_max):
    scaled = []
    for i in i_data:
        scaled.append(scale_f(i, n_max=n_max, n_min=n_min, c_min=c_min, c_max=c_max))
    
    return scaled

def smooth_func(x):
    h = 58.1392623
    c = 0
    b = 1.1
    #return (b**(-x + h)) + c # Inverse/decay
    return (b**(x + h)) + c

"""
Render
"""

def get_frames(frames, data, increase_count, increase_val):

    video_dir = os.path.join('video') # Get the path to the video.

    frames_list = []
    sample_index = 0
    x = 0
    for i in range(0, frames):
        # Clear console
        clear = lambda: os.system('clear')
        clear()
        
        # Progress
        print('frame: ', i, ' | ', str((i/frames) * 100), '%')

        get_linear_color(frame=i)

        # Create a frame:
        frame = Image.new('RGB', (300, 300), (0, 0, 0))
        draw = ImageDraw.Draw(frame)
        size = 300 # Holder -> TODO: Make this define the size of the frame at some point.

        # Create the circle:
        c = Circle(60)
        circles = c.get_circles()

        # Create the gradient:
        g = Gradient(startColor=(255, 0, 26), endColor=(205, 0, 255), isVerticle=True, distance=(60))
        g.cacl_increase()
        g.obtainM()

        # Sort out scaled G value for all circles:
        # Baso, I just want to get value x, if x is bigger than current x, replace.
        # If x is lower than current x, x - 1
 
        if (data[sample_index] > x):
            x = data[sample_index]
            increase_count += 1
            increase_val.append(abs(int(smooth_func(x=x))))
        else:
            if (x == -124):
                x == -124
            else:
                x = x - 0.5

        # Loop through the circles to draw the gradient circle.
        for r, circle in enumerate(circles):
            color = g.calculate_color(x_coord=r, y_coord=0)
            
            if (sample_index > len(data)):
                sample_index = len(data) - 1

            # Get a value to set 'G' value.
            # color[1] = abs((int(data[sample_index] * 255) * 2))
            color[1] = abs(int(smooth_func(x=x))) * 4
            t_color = tuple(color)

            # Index through the points in the circle to draw.
            for p in circle:
                draw.point((int(size/2+p[0]), int(size/2+p[1])),t_color)
        
        # Save the frame and append to the list.
        name = str(i) + '.jpg'
        frame.save(os.path.join(video_dir, name))
        frames_list.append(name)

        # Increase the sample index.
        if ((sample_index + 375) > len(data)):
            sample_index = len(data) - 1
        else:
            sample_index += 375

    return frames_list

def write_frames(frames, resampled, increase_count, increase_val):

    # Get the frames necesarry:
    frames = get_frames(frames=frames, data=resampled, increase_count=increase_count, increase_val=increase_val)

    # Store opened images (frames).
    img_arr = []

    # Loop through the frames:
    for filename in frames:

        # Open image:
        img = cv2.imread(os.path.join('video', filename))
        height, width, layers = img.shape # Get the dimensions.
        size = (width, height) # Gather the size.
        img_arr.append(img) # Append the image to the array.

    out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, size) # Create a video out object.

    # Write frames to 'out'.
    for i in range(len(img_arr)):
        out.write(img_arr[i])

    out.release() # Save the video.
    return None

def main():

    start_time = time.time()

    # Stats:
    intensity_increase_count = 0
    intensity_increase_val = []

    # Read the directory:
    music_dir = os.path.join('music')
    # songs = os.listdir(music_dir)

    # Import the song:
    y, sr = librosa.load(os.path.join(music_dir, 'flume-hollow.mp3'))

    # # Get the frames needed:
    # frames = song_length_to_frames(y=y, sr=sr, frames=60)

    # Scale the data:
    scaled_data = np.array(scale_data(i_data=y, n_max=0, n_min=-124, c_min=y.min(), c_max=y.max()))

    # print('frames for 60fps: ', frames) 
    input('...')
    write_frames(frames=14100, resampled=scaled_data, increase_count=intensity_increase_count, increase_val=intensity_increase_val)
    print('End Stats')
    print("--- %s seconds ---" % (time.time() - start_time))
    print('Intensity increases: ', intensity_increase_count)
    print('Increase values')
    input('press any key to show')
    for i in intensity_increase_val:
        print(i)
        print('----')



main()

# https://stackoverflow.com/questions/5294955/how-to-scale-down-a-range-of-numbers-with-a-known-min-and-max-value 
