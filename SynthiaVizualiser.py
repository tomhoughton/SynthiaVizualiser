""" Imports """
import os
from turtle import color
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time

# My imports:
from gradient import Gradient
from circle import Circle
from Song import Song
from visualise import Visualise
"""

Tasks:
- create a menu

"""


def main():
    print('╭━━━╮╱╱╱╱╱╱╭╮╭╮╱╱╱╱╱╱╭╮╱╱╭╮╱╱╱╱╱╱╱╱╭╮')
    print('┃╭━╮┃╱╱╱╱╱╭╯╰┫┃╱╱╱╱╱╱┃╰╮╭╯┃╱╱╱╱╱╱╱╱┃┃')
    print('┃╰━━┳╮╱╭┳━╋╮╭┫╰━┳┳━━╮╰╮┃┃╭╋━━┳╮╭┳━━┫┃╭┳━━┳━━┳━╮')
    print('╰━━╮┃┃╱┃┃╭╮┫┃┃╭╮┣┫╭╮┃╱┃╰╯┣┫━━┫┃┃┃╭╮┃┃┣┫━━┫┃━┫╭╯')
    print('┃╰━╯┃╰━╯┃┃┃┃╰┫┃┃┃┃╭╮┃╱╰╮╭┫┣━━┃╰╯┃╭╮┃╰┫┣━━┃┃━┫┃')
    print('╰━━━┻━╮╭┻╯╰┻━┻╯╰┻┻╯╰╯╱╱╰╯╰┻━━┻━━┻╯╰┻━┻┻━━┻━━┻╯')
    print('╱╱╱╱╭━╯┃')
    print('╱╱╱╱╰━━╯')

    print(' Choose a song to use: ')
    
    # Load the songs directory:
    music_dir = os.path.join('music')
    songs = os.listdir(music_dir)

    for i, song in enumerate(songs):
        print('[', i, ']', ' ', song)

    usr = int(input('Select the song you would like'))

    song = songs[usr]

    # Load the song:
    my_song = Song(song=song, music_path=music_dir, frame_rate=60, new_min=-124, new_max=0)

    # Create visualiser object:
    visualise = Visualise(frame_amount=my_song.frame_amount, data=my_song.scaled_data)

    # Firstly we need to create all individual frames:

    """ 
    How can we go about creating the statistics:
    """
    start_time = time.time() # Store the time at which rendering started.
    
    visualise.create_frames(visualise.frame_amount, my_song.scaled_data)
    smooth_val, song_val = visualise.write_video()
    
    time_to_compute = time.time() - start_time

    print("--- %s seconds ---" % (time_to_compute))
    plt.plot(smooth_val, color='green')
    plt.plot(song_val, color='red')
    plt.show()
    

main()