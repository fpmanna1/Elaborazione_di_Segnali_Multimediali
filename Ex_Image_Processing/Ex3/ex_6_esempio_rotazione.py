# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:44:42 2023

@author: nokia
"""


import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

from skimage.transform import warp 

plt.close('all')

x = np.float32(io.imread('lena.jpg'))
A = np.array([[np.cos(np.pi/4),np.sin(np.pi/4),0], [-np.sin(np.pi/4),np.cos(np.pi/4),0], [0,0,1]], dtype=np.float32)
y = warp(x, A, order = 1) 

# da notare che ruotiamo rispetto al punto (0,0) e non rispetto al centro
plt.subplot(1,2,1);
plt.imshow(x,clim=[0,255],cmap='gray'); plt.title('originale'); plt.subplot(1,2,2);
plt.imshow(y,clim=[0,255],cmap='gray'); plt.title('ruotata');