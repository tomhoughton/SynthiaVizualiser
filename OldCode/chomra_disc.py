# Imports:
import librosa
import librosa.display
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def seperate_h_s(data, sr):
    harm, percus = librosa.effects.hpss(data)

    return harm, percus

def main():
    data, sr = librosa.load('flume-hollow.mp3')
    print(data)
    data_h, data_p = seperate_h_s(data, sr)

    chroma = librosa.feature.chroma_cqt(y=data_h, sr=sr)
    plt.figure(figsize=(18,5))

    librosa.display.specshow(chroma, sr=sr, x_axis='time', y_axis='chroma', vmin=0, vmax=1)
    plt.title('Chromagram')
    plt.colorbar()
    plt.figure(figsize=(20,8))
    plt.show() 


main()