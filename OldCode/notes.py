#%%

from turtle import st
import librosa

#%%
data, sr = librosa.load('./music/flume-hollow.mp3')

print('Data Shape: ', data.shape)

# %%

print('Sample Rate: ', sr)

# %%

import matplotlib
import matplotlib.pyplot as plt

plt.plot(data)
plt.show()

# %%

print(sr)

#%%

y_8k = librosa.resample(data, orig_sr=sr, target_sr=60)

print(len(data))

#%%

sr / 60

# So every 367 frames


#%%
for i in y_8k:
    print(int(i))

#%%
import numpy as np
data.max()

#%%
data.min()
#%%

plt.plot(y_8k)
plt.show()

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



from gradient_cls import Gradient

g = Gradient(startColor=(76, 163, 217), endColor=(205, 255, 199), isVerticle=True, distance=200)

g.cacl_increase()
# %%
print(g.increaseOrDecrease)
# %%
g.obtainM()
print(g.m)
# %%

import numpy as np

# %%

def y(x):
    h = 58.1392623
    c = 0
    b = 1.1

    return (b**(-x + h)) + c



# %%
print(int(y(0)))
# %%

import matplotlib
import matplotlib.pyplot as plt

a = [1, 2, 5, 6, 2, 5]
b = [3, 7, 3, 1, 8, 2]

plt.plot(a)
plt.plot(b, color='green')
plt.show()

# %%
