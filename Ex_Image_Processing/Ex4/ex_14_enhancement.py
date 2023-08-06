# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:06:58 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = np.float64(io.imread('luna.jpg')) 
# Di seguito la maschera del filtro che realizza il Laplaciano 
# secondo la definizione di derivata indicata nel testo 
h = np.array([[0,0,1,0,0],[0,0,0,0,0],[1,0,-4,0,1],[0,0,0,0,0],[0,0,1,0,0]],dtype=np.float64)
h2 = np.array([[0,1,0],[1,-4,1],[0,1,0]], dtype = np.float32)

y = ndi.correlate(x,h)
y_enhanc = x-y
y2 = ndi.correlate(x, h2)
y2_enhanc = x-y2

plt.figure(1); 
plt.subplot(1,2,1)
plt.imshow(y_enhanc, clim=[0,255],cmap='gray');
plt.subplot(1,2,2)
plt.imshow(y2_enhanc, clim = [0,255], cmap= 'gray')