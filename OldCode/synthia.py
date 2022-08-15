# So we basically need to get the data in and just change pixels.
# We also need to work out the amount of frames in the time frame
# And how to export audio with the video.

from turtle import width
import librosa
import librosa.display
import numpy as np
import os
from PIL import Image
import cv2


def song_length_to_frames(y, sr, frames):

    # Theory is:
    # If a video is 60 fps
    # Then fps * seconds of song.

    # Get the duration in seconds:
    duration = int(librosa.get_duration(y=y, sr=sr))
    frames = duration * 60
    return frames

def linear_scale_factor(frames, max_val, min):
    return max_val / frames

def get_linear_color(frame, scale):
    return frame * scale

def get_frames(frames, scale):
    video_dir = os.path.join('video')

    frames_list = [] # Store all new frames in list.

    for i in range(0, frames):
        get_linear_color() 

def write_frames(frames, scale):
    # Create the frames:
    frames = get_frames(frames=frames, scale=scale)
    img_arr = []
    for filename in frames:
        img = cv2.imread(os.path.join('video', filename))
        height, width, layers = img.shape
        size = (width, height)
        img_arr.append(img)

    
    out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, size)
    for i in range(len(img_arr)):
        out.write(img_arr[i])
    out.release()

    print('done')

    return None

def main():

    # Get music directory:
    music_dir = os.path.join('music')

    # Import the song: 
    y, sr = librosa.load(os.path.join(music_dir, 'flume-hollow.mp3'))

    # Get the frames needed:
    frames = song_length_to_frames(y, sr, frames)

    # Figure out scale factor:
    scale = linear_scale_factor(frames=frames, max_val=255, min=None)

    # Now we need to write the frames:
    write_frames(frames=frames)

     