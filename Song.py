import librosa
import os
import numpy as np

class Song:
    def __init__(self, song, music_path, frame_rate, new_min, new_max):
        y, sr = librosa.load(os.path.join(music_path, song))

        self.y = y
        self.sr = sr
        self.frame_amount = self.song_length_to_frames(self.y, self.sr, frame_rate)

        # Scale the data:
        self.current_min = self.y.min()
        self.current_max = self.y.max()
        self.scaled_data = self.scale_data(
            self.y, 
            new_max=new_max, 
            new_min=new_min, 
            current_min=self.current_min, 
            current_max=self.current_max
        )
        return None
    
    def song_length_to_frames(self, y, sr, frame_rate) -> int:
        """Return the amount of frames needed for the video

        Args:
            y (np.array([int])): the audio samples from librosa.
            sr (int): sample rate from librosa.
            frame_rate (int): frame rate of the video.

        Returns:
            int: frames required
        """
    
        duration = int(librosa.get_duration(y=y, sr=sr))
        rtn_frames = duration * frame_rate # Multiply by  frame rate.
        return rtn_frames


    def scale_data(self, input, new_max, new_min, current_min, current_max) -> np.array([int]):
        """Scales the input data to a new min and max to allow for the intensity function.

        Args:
            input (np.array([int])): data from librosa.

        Returns:
            np.array([int]): scaled data 
        """

        scaled_data = np.zeros(len(input))  
        
        # Scale function:
        scale_f = lambda x, n_max, n_min, c_max, c_min : ((n_max - n_min) * (x - c_min) / (c_max - c_min)) + n_min

        for i, val in enumerate(input):
            scaled_data[i] = scale_f(x=val, n_max=new_max, n_min=new_min, c_min=current_min, c_max=current_max)

        return scaled_data


    