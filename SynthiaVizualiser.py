""" Imports """
import os
import numpy as np

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
    visualise.create_frames(visualise.frame_amount, my_song.scaled_data)
    visualise.write_video()




        
main()