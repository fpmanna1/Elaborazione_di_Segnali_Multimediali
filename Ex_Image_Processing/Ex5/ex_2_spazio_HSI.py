# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:48:45 2023

@author: plett
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from color_convertion import rgb2hsi, hsi2rgb

plt.close('all')

x = io.imread('colori.jpg') 
x = np.float64(x)/255 

x_hsi = rgb2hsi(x)

Hx = x_hsi[:,:,0] # tinta
Sx = x_hsi[:,:,1] # saturazione
Ix = x_hsi[:,:,2] # intensità


plt.figure();
plt.subplot(1,3,1); 
plt.imshow(Hx,clim=[0,1],cmap='gray'); 
plt.title('Tinta'); 
plt.subplot(1,3,2); 
plt.imshow(Sx,clim=[0,1],cmap='gray'); 
plt.title('Saturazione');
# 0 non ho saturazione quindi ho grigio
# 1 ho un colore pennarello
plt.subplot(1,3,3);
plt.imshow(Ix,clim=[0,1],cmap='gray'); 
plt.title('Luminosità');

x = rgb2hsi(x_hsi)

img = x[:,:,2]

H1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
H2 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
#H1_3D = np.expand_dims(H1, -1)
#H2_3D = np.expand_dims(H2,-1)


Y1 = ndi.correlate(img, H1)
Y2 = ndi.correlate(img, H2)

Y = np.abs(Y1) + np.abs(Y2)

mask = Y > 1.75*np.mean(Y)

plt.figure()
plt.imshow(Y, clim = None, cmap = 'gray')


