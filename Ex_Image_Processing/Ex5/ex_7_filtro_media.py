# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 17:47:02 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
import skimage

from skimage.exposure import equalize_hist
from color_convertion import rgb2hsi, hsi2rgb

plt.close('all')

# filtro di smoothing di dimensione 5x5, prima in RGB e poi in HSI

x = np.float32(io.imread('lenac.jpg'))/255

R = x[:,:,0]
G = x[:,:,1]
B = x[:,:,2]

K = 5

Ry = ndi.uniform_filter(R, (K,K), mode = 'reflect')
Gy = ndi.uniform_filter(G, (K,K), mode = 'reflect')
By = ndi.uniform_filter(B, (K,K), mode = 'reflect')

y = np.stack((Ry,Gy,By), -1)

from skimage.color import rgb2yuv, yuv2rgb 

w = rgb2yuv(x) 
w[:,:,0] = ndi.uniform_filter(w[:,:,0], (5,5)) 
z = yuv2rgb(w) 

plt.figure()
plt.subplot(1,3,1)
plt.title('Immagine originale')
plt.imshow(x)
plt.subplot(1,3,2)
plt.title('Filtro media in RGB')
plt.imshow(y)
plt.subplot(1,3,3)
plt.title('Filtraggio in YUV')
plt.imshow(z)