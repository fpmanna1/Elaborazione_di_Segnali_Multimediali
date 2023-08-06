# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:46:49 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = np.float32(io.imread('quadrato.jpg'))

plt.figure(1)
plt.title('Immagine originale')
plt.imshow(x, cmap = 'gray', clim = [0,255])

# definisco le maschere per individuare le linee in tutte le direzioni

a = [[-1,-1,-1], [2, 2 ,2], [-1,-1,-1]] # linea orizzontale
b = [[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]] # linea verticale
c = [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]] # linea obliqua
d = [[-1, -1, 2], [-1, 2, -1], [2, -1, -1]] # linea obliqua

ya = ndi.correlate(x, a)
yb = ndi.correlate(x, b)
yc = ndi.correlate(x, c)
yd = ndi.correlate(x, d)

plt.figure(2, figsize=(10, 10))
plt.subplot(1, 4, 1)
plt.imshow(ya, clim = [0,1], cmap = 'gray')
plt.subplot(1, 4, 2)
plt.imshow(yb, clim = [0,1], cmap = 'gray')
plt.subplot(1, 4, 3)
plt.imshow(yc, clim = [0,1], cmap = 'gray')
plt.subplot(1, 4, 4)
plt.imshow(yd, clim = [0,1], cmap = 'gray')



# ottenere un'unica mappa a partire dalle singole mappe

concat = np.stack((ya, yb, yc, yd), axis = -1)

immagine_massimi1 = np.max(concat, axis=-1)
plt.figure(3)
plt.imshow(immagine_massimi1,clim=None,cmap='gray'); 
