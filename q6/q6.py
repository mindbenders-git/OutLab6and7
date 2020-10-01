##Do it here##
import numpy as np
import matplotlib.pyplot as plt

x = np.load('decode_this.npy')

key_img = (x - x.min()) / (x.max() - x.min())

plt.imshow(key_img)
plt.savefig('result.png')

#ref --> https://academic.mu.edu/phys/matthysd/web226/Lab01.htm
