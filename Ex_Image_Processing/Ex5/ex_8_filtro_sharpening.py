# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:27:57 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
import skimage

from skimage.exposure import equalize_hist
from color_convertion import rgb2hsi, hsi2rgb
from skimage.color import rgb2yuv, yuv2rgb 

plt.close('all')

x = np.float32(io.imread('fiori.jpg'))/255

# applico il filtro laplaciano

H = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], dtype = np.float32)

# estendo la maschera a 3 dimensioni
H_3D = np.expand_dims(H, -1)


# ENHANCEMENT IN RGB

y = ndi.correlate(x, H_3D)

plt.figure(1)
plt.title('Immagine originale')
plt.imshow(x)

plt.figure(2)
plt.title('Enhancement in RGB')
plt.imshow(y)

# ENHANCEMENT IN HSI

w = rgb2hsi(x) 
w[:,:,2] = ndi.correlate(w[:,:,2], H) # applico il filtro solo per la componente luminosità
z = hsi2rgb(w) 
plt.figure(3); plt.imshow(z);
plt.title('Enhancement in HSI');

