# So we basically need to get the data in and just change pixels.
# We also need to work out the amount of frames in the time frame
# And how to export audio with the video.

import librosa
import librosa.display
import numpy as np
import os


def song_length_to_frames(y, sr, frames):

    # Theory is:
    # If a video is 60 fps
    # Then fps * seconds of song.



    print()

def main():

    # Read the directory:
    music_dir = os.path.join('music')
    # songs = os.listdir(music_dir)

    # Import the song:
    y, sr = librosa.load(os.path.join(music_dir, 'flume-hollow.mp3'))

    # Get the frames needed:
    frames = song_length_to_frames(y=y, sr=sr, frames=60)

main()