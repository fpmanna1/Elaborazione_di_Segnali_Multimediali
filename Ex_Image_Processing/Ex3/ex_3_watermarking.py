# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:26:39 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

from bitop import bitset 
from bitop import bitget

plt.close('all')

#x = io.imread('lena.jpg') # dimensione: 512x512, devo fare un reshape di Lena a 350x350

img = np.fromfile('lena.y',np.uint8)
img = np.reshape(img,(512, 512))
plt.figure(1); plt.imshow(img, clim=[0,255], cmap='gray')
plt.title('Immagine originale')

mar = np.fromfile('marchio.y',np.uint8)
mar = np.reshape(mar,(350,350))
plt.figure(2); plt.imshow(mar, clim=[0,1], cmap='gray')
plt.title('watermark')


img[:350,:350] = bitset(img[:350,:350],0,mar)
plt.figure(3); plt.imshow(img, clim=[0,255], cmap='gray')


y = bitget(img,0)
plt.figure(4); plt.imshow(y, clim=None, cmap='gray')


