# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:23:51 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage

from skimage.transform import warp 

plt.close('all')

def media(x, k):
    h = np.ones((k,k))/(k**2) 
    y = ndi.correlate(x, h, mode='reflect')
    return y
    

x = np.float64(io.imread('space.jpg')) 
plt.figure(1); plt.imshow(x,clim=[0,255],cmap='gray'); plt.title('immagine senza modifiche')

y = media(x, 20)

# la dim. della finestra su cui calcolo la media determina la grandezza degli oggetti
# che vedrò in output. Più è grande, più gli oggetti piccoli verranno mediati su una 
# finestra più grande, restituendo un valore piccolo, che verrà scartato nella
# successiva fase di thresholding


th = (25/100)*np.max(y) # soglia = 25 per cento del valore max 
z = y>th # calcolo la maschera 
plt.figure(2); plt.imshow(z, clim=[0,1],cmap='gray'); plt.title('maschera')

w = z*y; # risultato dell’elaborazione

plt.figure(3); plt.imshow(w,clim=[0,255],cmap='gray'); plt.title('immagine finale')