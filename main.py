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

"""
Image
"""
def song_length_to_frames(y, sr, frames):

    # Theory is:
    # If a video is 60 fps
    # Then fps * seconds of song.

    # Get the duration in seconds:
    duration = int(librosa.get_duration(y=y, sr=sr))
    frames = duration * 60
    return frames

def create_image():

    img = Image.new('RGB', (300, 200), (255, 0, 0))
    img.show()

def get_linear_color(frame):
    m = 0.018085106
    x = frame

    return x * m

def get_frames(frames):

    video_dir = os.path.join('video')

    frames_list = []

    for i in range(0, frames):
        # print('frame: ', i, ' r: ', get_linear_color(i))
        get_linear_color(frame=i)
        frame = Image.new('RGB', (300, 200), (int(get_linear_color(i)), 0, 0))
        name = str(i) + '.jpg'
        frame.save(os.path.join(video_dir, name))
        frames_list.append(name)

    return frames_list

def write_frames(frames):

    frames = get_frames(frames=frames)
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

    return '' 


def main():
    # Read the directory:
    music_dir = os.path.join('music')
    # songs = os.listdir(music_dir)

    # Import the song:
    y, sr = librosa.load(os.path.join(music_dir, 'flume-hollow.mp3'))

    # Get the frames needed:
    frames = song_length_to_frames(y=y, sr=sr, frames=60)

    print('frames for 60fps: ', frames)

    write_frames(frames=14100)


main()