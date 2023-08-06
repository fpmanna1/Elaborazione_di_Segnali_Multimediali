# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:11:50 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage

from skimage.transform import warp 

plt.close('all')

def smooth(x):
    h = np.array([[1,2,1,],[2,4,2],[1,2,1]], dtype=np.float32)/16
    y = ndi.correlate(x, h, mode='reflect')
    
    return y

x = np.float64(io.imread('luna.jpg')) 
y = smooth(x)

plt.figure(1); 
plt.subplot(1,2,1)
plt.imshow(x,clim=[0,255],cmap='gray')
plt.title('immagine senza filtro')
plt.subplot(1,2,2)
plt.imshow(y,clim=[0,255],cmap='gray')
plt.title('immagine con filtro')
