# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:27:42 2023

@author: plett
"""

import skimage.data as data
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

x = np.float64(data.brick())

plt.figure();
plt.imshow(x, clim = [0, 255], cmap='gray');

h0 = np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=np.float64) 
h1 = np.array([[0,1,0],[0,-1,0],[0,0,0]], dtype=np.float64) 
h2 = np.array([[0,0,1],[0,-1,0],[0,0,0]], dtype=np.float64) 
h3 = np.array([[0,0,0],[0,-1,1],[0,0,0]], dtype=np.float64) 
h4 = np.array([[0,0,0],[0,-1,0],[0,0,1]], dtype=np.float64) 
h5 = np.array([[0,0,0],[0,-1,0],[0,1,0]], dtype=np.float64) 
h6 = np.array([[0,0,0],[0,-1,0],[1,0,0]], dtype=np.float64)
h7 = np.array([[0,0,0],[1,-1,0],[0,0,0]], dtype=np.float64)

b0 = ndi.correlate(x, h0) >= 0 
b1 = ndi.correlate(x, h1) >= 0 
b2 = ndi.correlate(x, h2) >= 0 
b3 = ndi.correlate(x, h3) >= 0 
b4 = ndi.correlate(x, h4) >= 0 
b5 = ndi.correlate(x, h5) >= 0 
b6 = ndi.correlate(x, h6) >= 0
b7 = ndi.correlate(x, h7) >= 0

y = b0 + 2*b1 + 4*b2 + 8*b3 + 16*b4 + 32*b5 + 64*b6 + 128*b7
# la variabile y contiene le descrizioni locali

plt.figure(); 
plt.imshow(y, clim=[0,255], cmap='gray'); 
plt.title('immagine LBP');

# possiamo identificare le patch uniformi sapendo che la descrizione
# relativa è 0 o 255

mappa_uniformi = (y==0) | (y==255) 
plt.figure(); plt.imshow(mappa_uniformi, clim=[0,1], cmap='gray');
plt.title('mappa delle patch uniformi');