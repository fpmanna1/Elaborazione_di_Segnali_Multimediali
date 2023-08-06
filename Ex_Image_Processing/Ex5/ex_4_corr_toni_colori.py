# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:05:02 2023

@author: plett
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io

plt.close('all')

x = io.imread('montagna.jpg') 
x = np.float64(x)/255 
plt.figure(1); plt.imshow(x); plt.title('Immagine originale'); gamma = 0.6;

# Elaborazione in RGB 
y = x ** gamma 

# in alternativa
# Ry = Rx ** 0.5
# Gy = Gx ** 0.5
# By = Bx ** 0.5

# y = np.stack((Ry, Gy, By),2)
# l'indici degli assi partono da zero
# voglio concatenare sull'ultimo asse

plt.figure(2); plt.imshow(y); plt.title('Elaborazione in RGB');

# Elaborazione in HSI 
from color_convertion import rgb2hsi, hsi2rgb 

# in alternativa
"""
Hz = Hx
Sz = Sx
Iz = Ix
z_hsi = np.stack((Hz, Sz, Iz), 2)
z = hsi2rgb(z_hsi)
"""

# lavorare solo sull'intensità preserva il colore

w = rgb2hsi(x) 

w[:,:,2] = w[:,:,2] ** gamma 
z = hsi2rgb(w) 
plt.figure(3); plt.imshow(z);
plt.title('Elaborazione in HSI');