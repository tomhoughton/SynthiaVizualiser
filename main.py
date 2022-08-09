# So we basically need to get the data in and just change pixels.
# We also need to work out the amount of frames in the time frame
# And how to export audio with the video.

from turtle import width
import librosa
import librosa.display
import numpy as np
import os
from PIL import Image, ImageDraw
import cv2
from gradient import Gradient
from circle import Circle

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

def get_frames(frames, data):

    video_dir = os.path.join('video')


    frames_list = []
    sample_index = 0
    for i in range(0, frames):
        clear = lambda: os.system('clear')
        clear()
        print('frame: ', i, ' | ', str((i/frames) * 100), '%')
        get_linear_color(frame=i)
        frame = Image.new('RGB', (300, 300), (0, 0, 0))
        draw = ImageDraw.Draw(frame)
        size = 300

        # Create the circle:
        c = Circle(60)
        circles = c.get_circles()

        # Create the gradient:
        g = Gradient(startColor=(255, 0, 26), endColor=(205, 0, 255), isVerticle=True, distance=(60))
        g.cacl_increase()
        g.obtainM()

        for r, circle in enumerate(circles):
            color = g.calculate_color(x_coord=r, y_coord=0)
            
            if (sample_index > len(data)):
                sample_index = len(data) - 1


            color[1] = abs((int(data[sample_index] * 255) * 2))

            t_color = tuple(color)
            for p in circle:
                draw.point((int(size/2+p[0]), int(size/2+p[1])),t_color)
        
        name = str(i) + '.jpg'
        frame.save(os.path.join(video_dir, name))
        frames_list.append(name)
        sample_index += 375

    return frames_list

def write_frames(frames, resampled):

    frames = get_frames(frames=frames, data=resampled)
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
    #y_60 = librosa.resample(y, orig_sr=sr, target_sr=60)


    print('Resampled')
    # print(y_60)

    # Get the frames needed:
    frames = song_length_to_frames(y=y, sr=sr, frames=60)

    print('frames for 60fps: ', frames)

    write_frames(frames=14100, resampled=y)


main()