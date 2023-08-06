# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:05:12 2023

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

"""
EX. Variazione del colore. 
Considerate l’immagine azzurro.jpg, dove `e presente un 
accappatoio azzurro, e generate l’immagine Rosso.jpg, in cui solo l’accappatoio 
diventa rosso. A tal fine, passate nello spazio di colore HSI, individuate 
la regione dell’immagine occupata dall’accappatoio in base ai suoi valori di
tinta, saturazione e luminanza, e solo in tale regione operate una opportuna 
variazione della sola tinta.
"""

x = np.float32(io.imread('azzurro.jpg'))/255

# passaggio nello spazio hsi
x_hsi = rgb2hsi(x)

# estrazione tinta, saturazione ed intensità
Hx = x_hsi[:,:,0]
Sx = x_hsi[:,:,1]
Ix = x_hsi[:,:,2]

# visualizzo separatamente le componenti
plt.figure()
plt.subplot(1,3,1); plt.title('Tinta'); plt.imshow(Hx)
plt.subplot(1,3,2); plt.title('Saturazione'); plt.imshow(Sx)
plt.subplot(1,3,3); plt.title('Intensità'); plt.imshow(Ix)


mask = (0.35<Hx) & (Hx<0.66) & (0.20<Sx) & (Sx<0.80) & (Ix>0.35) 
Hx = Hx + 0.38*mask
Hx = Hx % 1.0 # funzione modulo per riportare H nel range [0,1] 
x_hsi[:,:,0] = Hx 
z = hsi2rgb(x_hsi)

plt.figure(3); plt.subplot(1,3,1); plt.imshow(x); plt.title('Immagine originale'); 
plt.subplot(1,3,2); plt.imshow(mask,clim=[0,1],cmap='gray'); plt.title('Maschera per la selezione'); 
plt.subplot(1,3,3); plt.imshow(z); plt.title('Risultato');