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

# My imports:
from gradient import Gradient
from circle import Circle

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

def get_frames(frames, data):

    video_dir = os.path.join('video') # Get the path to the video.

    frames_list = []
    sample_index = 0
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

        # Loop through the circles to draw the gradient circle.
        for r, circle in enumerate(circles):
            color = g.calculate_color(x_coord=r, y_coord=0)
            
            if (sample_index > len(data)):
                sample_index = len(data) - 1

            # Get a value to set 'G' value.
            color[1] = abs((int(data[sample_index] * 255) * 2))
            t_color = tuple(color)

            # Index through the points in the circle to draw.
            for p in circle:
                draw.point((int(size/2+p[0]), int(size/2+p[1])),t_color)
        
        # Save the frame and append to the list.
        name = str(i) + '.jpg'
        frame.save(os.path.join(video_dir, name))
        frames_list.append(name)

        # Increase the sample index.
        sample_index += 375

    return frames_list

def write_frames(frames, resampled):

    # Get the frames necesarry:
    frames = get_frames(frames=frames, data=resampled)

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

    # Read the directory:
    music_dir = os.path.join('music')
    # songs = os.listdir(music_dir)

    # Import the song:
    y, sr = librosa.load(os.path.join(music_dir, 'flume-hollow.mp3'))

    # Get the frames needed:
    frames = song_length_to_frames(y=y, sr=sr, frames=60)

    print('frames for 60fps: ', frames) 

    write_frames(frames=14100, resampled=y)


main()