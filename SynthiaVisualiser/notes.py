#%%
print('Hello')
# %%
import librosa 
import os
# %%
m = os.path.join('flume-hollow.mp3')
y, sr = librosa.load(m)
print(sr)
print(y.max()) 
#%% 

len(y)

#%%
print(y)


#%%

perc = len(y) * 0.01

#%%
import matplotlib.pyplot as plt
# Part of the time series:
y_part = y[:int(perc)]

plt.plot(y_part)
plt.show()

# %%

y.max()

#%%

y.min()

#%%
import numpy as np
# Scale the values within the time series data:
def scale_data(input, new_max, new_min, current_min, current_max) -> np.array([float]):
    """Scales the input data to a new min and max to allow for the animation functions

    Args:
        inpt (_type_): _description_
    """
    # Create an empty array to scale the data:
    scaled_data = np.zeros(len(input), dtype=float)

    # Scale Lambda Function:    
    scale_f = lambda x, n_max, n_min, c_max, c_min : ((n_max - n_min) * (x - c_min) / (c_max - c_min)) + n_min

    for i, val in enumerate(input):
        scaled_data[i] = scale_f(val, new_max, new_min, current_min, current_max)

    return scaled_data

#%%

print('Original Min and Max: ', y.min(), y.max())

scaled_data = scale_data(y, 255, 0, y.min(), y.max())

print('new min and max: ', scaled_data.min(), scaled_data.max())

#%%


# %%

from Animator import Animator
anim = Animator()
curr_anim = 0
out = []
for i in y:
    anim_v = anim.get_value_eq01(i)
    if anim_v > curr_anim:
        curr_anim = anim_v
    else:
        curr_anim -= 5
    out.append(curr_anim)

import matplotlib.pyplot as plt
plt.plot(out)
plt.figure(figsize=(20, 20), dpi=100)
plt.show()