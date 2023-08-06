# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:25:24 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x1 = np.float64(io.imread('lena.jpg')) 


P = 500; Q = 500; 
for k in range(5,20,5): 
    h = np.ones((k,k)) / (k**2) 
    H = np.fft.fft2(h,(P,Q)) 
    H = np.abs(np.fft.fftshift(H))
    plt.figure(); plt.imshow(H, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
    plt.title('Risposta in frequenza del filtro media aritmetica per k=%d' % k)