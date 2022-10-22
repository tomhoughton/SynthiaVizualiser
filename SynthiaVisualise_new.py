# Imports:
import os
import PIL.Image, PIL.ImageDraw


def gradient_test():
    print('Gradient Test')

    width, height = (1000, 1000)

    img = PIL.Image.new("RGB", (width, height), (10, 10, 10))
    
    for y in range(0, height):
        for x in range(0, width):
            color = (255, 0, 0)
            img.putpixel((x, y), color)

    img.show()


def circle_test():
    print('Circle test')


def circle_anim_test():
    print('Circle Anime test')



def main():
    print('╭━━━╮╱╱╱╱╱╱╭╮╭╮╱╱╱╱╱╱╭╮╱╱╭╮╱╱╱╱╱╱╱╱╭╮')
    print('┃╭━╮┃╱╱╱╱╱╭╯╰┫┃╱╱╱╱╱╱┃╰╮╭╯┃╱╱╱╱╱╱╱╱┃┃')
    print('┃╰━━┳╮╱╭┳━╋╮╭┫╰━┳┳━━╮╰╮┃┃╭╋━━┳╮╭┳━━┫┃╭┳━━┳━━┳━╮')
    print('╰━━╮┃┃╱┃┃╭╮┫┃┃╭╮┣┫╭╮┃╱┃╰╯┣┫━━┫┃┃┃╭╮┃┃┣┫━━┫┃━┫╭╯')
    print('┃╰━╯┃╰━╯┃┃┃┃╰┫┃┃┃┃╭╮┃╱╰╮╭┫┣━━┃╰╯┃╭╮┃╰┫┣━━┃┃━┫┃')
    print('╰━━━┻━╮╭┻╯╰┻━┻╯╰┻┻╯╰╯╱╱╰╯╰┻━━┻━━┻╯╰┻━┻┻━━┻━━┻╯')
    print('╱╱╱╱╭━╯┃')
    print('╱╱╱╱╰━━╯')

    print('Please select whether you would like to go to tests or main: ')
    
    inp = input('1: main, 2: gradient test, 3: circle test, 4: circle animation test')

    if inp == '1':
        print('Main')
    elif inp == '2':
        gradient_test()
    elif inp == '3':
        circle_test()
    elif inp == '4':
        circle_anim_test()        


    print(' Choose a song to use: ')

    # Load the songs directory:
    music_dir = os.path.join('music')
    songs = os.listdir(music_dir)

    for i, song in enumerate(songs):
        print('[', i, ']: ', song)

    # Get some use input;
    usr = int(input('Select the song you would like to use'))
    
    
if __name__ == "__main__": 
    main()