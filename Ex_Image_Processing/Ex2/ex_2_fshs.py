# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:48:19 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

def fshs(x): 
    """
    effettua il Full-scale Histogram Stretch 
    """
    m = np.min(x) 
    M = np.max(x) 
    y = 255*(x - m)/(M - m)
    return y

x = np.float32(io.imread('angiogramma.jpg')) 

plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')

n, b = np.histogram(x, np.arange(257)); # istogramma 
plt.figure(2); plt.bar(np.arange(256), n); # grafico a barre 
plt.axis([0,255,0,1.1*np.max(n)]); # estremi per ascisse e ordinate

z = fshs(x)

plt.figure(3)
plt.imshow(z, clim=[0,255], cmap='gray')

n_2, b_2 = np.histogram(z, np.arange(257)); # istogramma 
plt.figure(4); plt.bar(np.arange(256), n_2); # grafico a barre 
plt.axis([0,255,0,1.1*np.max(n_2)]); # estremi per ascisse e ordinate
