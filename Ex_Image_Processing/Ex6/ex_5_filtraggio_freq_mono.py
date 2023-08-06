# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:33:27 2023

@author: plett
"""

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

plt.close('all')

# proviamo a determinare attraverso la DFT e la IDFT la risposta
# del filtro con x=[1,2,3,4] e h=[1,1,1]
# bisogna calcolare la DFT su almeno 4 + 3 - 1 = 6 punti
# per garantire la correttezza del risultato

x = np.array([1,2,3,4], dtype = np.float64) # vettore ingresso
h = np.array([1,1,1], dtype = np.float64) # risposta impulsiva

# y = np.convolve(x, h)

X = np.fft.fft(x, 6) # realizza la DFT su 6 punti
H = np.fft.fft(h, 6)

Y = X * H

y = np.fft.ifft(Y, 6)

print(y)
