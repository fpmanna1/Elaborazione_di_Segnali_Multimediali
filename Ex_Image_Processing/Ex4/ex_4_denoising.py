# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:44:29 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage

from skimage.transform import warp 

plt.close('all')

x = np.float64(io.imread('lena.jpg')) 
plt.figure(1); plt.imshow(x,clim=[0,255],cmap='gray'); plt.title('immagine originale')

M, N = x.shape
d=20
n = d*np.random.randn(M,N)

z = x + n # aggiungo il rumore gaussiano alla foto

plt.figure(2); plt.imshow(z,clim=[0,255],cmap='gray'); plt.title('immagine rumorosa')

# miglioramento dell'immagine attraverso filtro media

def media(x, k):
    mask = np.ones((k,k))/(k**2)
    y = ndi.correlate(x, mask, mode = 'reflect')
    return y
  

z = media(z, 3)

plt.figure(3)
plt.title('immagine ripulita')
plt.imshow(z, cmap = 'gray', clim = [0,255])


# calcolo dell'errore quadratico medio
# diff dell'immagine pixel per pixel, e sommiamo tutti i valori

MSE = np.sum((x-z)**2)/(M*N)

# a livello di MSE, il filtro 3x3 garantisce l'MSE più basso




print(MSE)