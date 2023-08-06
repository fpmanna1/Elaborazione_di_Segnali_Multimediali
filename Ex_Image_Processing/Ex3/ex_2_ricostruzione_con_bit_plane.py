# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:17:53 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

from bitop import bitset 

plt.close('all')

x = io.imread('filamento.jpg') 


n = 3 # Numero di bit-plane da annullare 
y = np.copy(x) 
for i in range(n): # i pù grande, bit più significativo
    y = bitset(y, i, 0)
plt.figure() 
plt.subplot(1,2,1)
plt.imshow(x, clim=[0,255],cmap='gray')
plt.title('Immagine originale')

plt.subplot(1,2,2)
plt.imshow(y, clim=[0,255],cmap='gray')
plt.title('Rappresentazione con i primi %d bitplane' % (8-n)) # a partire dal più significativo