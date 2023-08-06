# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:43:52 2023

@author: plett
"""

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

plt.close('all')

x = np.float64(io.imread('lena.jpg'))

h = np.array([[1,0,-1],[2,0,-2],[1,0,-1]], dtype = np.float64)

M,N = x.shape # restituisce le dimensioni dell'array
A,B = h.shape

# stabiliamo su quanti punti fare la DFT
P = M + A - 1 # righe
Q = N + B - 1 # colonne

X = np.fft.fft2(x, (P,Q))
H = np.fft.fft2(h, (P,Q))

Y = H * X

y = np.real(np.fft.ifft2(Y))
# il risultato della IDFT dovrebbe essere reale, ma a causa di errori
# di precisione c'è una piccola parte immaginaria

plt.figure()
plt.title('Immagine filtrata')
plt.imshow(y, clim = None, cmap = 'gray')

