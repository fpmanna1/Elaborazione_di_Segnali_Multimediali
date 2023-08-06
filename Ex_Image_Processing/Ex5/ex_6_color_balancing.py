# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:54:12 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io

plt.close('all')

x = io.imread('foto.jpg') 
x = np.float64(x)/255

c = 1 - x[:,:,0] # ottengo il ciano dal rosso
# passo allo spazio CMY, ma considero solo la componente di CIANO
c = c ** 1.8 # diminuisco il ciano
# c = c-0.1
y = np.stack((1-c, x[:,:,1],x[:,:,2]), -1) # con 1-c torno in RGB e indico il rosso

"""
in alternativa posso elaborare direttamente in RGB
Rx = x[:,:,0]
Gx = x[:,:,1]
By = x[:,:,2]

Ry = Rx ** 0.7  # aumentando il rosso diminuisce il ciano
Gy = Gx ** 1.0
By = Bx ** 1.0

# in alternativa posso assegnare 1.0, 1.3 e 1.3
"""


z = io.imread('foto_originale.tif') 
z = np.float64(z)/255

plt.figure(1)
plt.subplot(1,3,1); plt.imshow(x); plt.title('troppo ciano') 
plt.subplot(1,3,2); plt.imshow(y); plt.title('immagine elaborata');
plt.subplot(1,3,3); plt.imshow(z); plt.title('immagine originale');

