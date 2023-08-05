# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:30:41 2023

@author: nokia
"""

# attiva la modalita interattiva di matplotlib %matplotlib qt
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = np.float32(io.imread('mammografia.jpg')) 

plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray')

y = 255-x
plt.figure(2)
plt.imshow(y, clim=[0,255], cmap='gray')

# salvataggio immagine sul disco

y = np.uint8(y)
io.imsave('negativo_mammografia.jpg',y , quality=10)