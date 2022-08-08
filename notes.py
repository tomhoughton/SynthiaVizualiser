#%%

import librosa

#%%
data, sr = librosa.load('flume-hollow.mp3')

print('Data Shape: ', data.shape)

# %%

print('Sample Rate: ', sr)

# %%

import matplotlib
import matplotlib.pyplot as plt

plt.plot(data)
plt.show()

# %%

print(data)

# %%
import librosa.display
spec = librosa.feature.melspectrogram(y=data, sr=sr)
librosa.display.specshow(spec, y_axis='mel', x_axis='s', sr=sr)
plt.colorbar() # This doesn't give much information.
# Mel is used to display pitch in a more regularized distribution.

# %%
import numpy as np
# We need to convert the amplitude squared to decibels.
db_spec = librosa.power_to_db(spec, ref=np.max)
librosa.display.specshow(db_spec, y_axis='mel', x_axis='s', sr=sr)
plt.colorbar()
# %%

from IPython.display import Audio
Audio(data=data, rate=sr)

#%%

# Split audio into harmonics and percussive:
data_harm, data_perc = librosa.effects.hpss(data)

spec_h = librosa.feature.melspectrogram(data_harm, sr=sr)
spec_p = librosa.feature.melspectrogram(data_perc, sr=sr)

db_spec_h = librosa.power_to_db(spec_h,ref=np.max)
db_spec_p = librosa.power_to_db(spec_p,ref=np.max)

#%%
librosa.display.specshow(db_spec_h, y_axis='hz', x_axis='s', sr=sr)

# %%
librosa.display.specshow(db_spec_p, y_axis='hz', x_axis='s', sr=sr)

# %%


# %%

chroma.shape

# %%
print(chroma)

# %%
# https://medium.com/@patrickbfuller/librosa-a-python-audio-libary-60014eeaccfb 
# %%