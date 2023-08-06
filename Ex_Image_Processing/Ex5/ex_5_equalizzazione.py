# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:12:41 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import skimage

from skimage.exposure import equalize_hist
plt.close('all')

x = np.float32(io.imread('volto.tiff'))/255

# equalizzazione in RGB

R = x[:,:,0]
G = x[:,:,1]
B = x[:,:,2]

Rmod = equalize_hist(R)
Gmod = equalize_hist(G)
Bmod = equalize_hist(B)

y1 = np.stack((Rmod,Gmod,Bmod), 2)

# equalizzazione in HSI

# converto da rgb ad hsi

from color_convertion import rgb2hsi, hsi2rgb

x_hsi = rgb2hsi(x)

# lavoro solo sulla terza banda (intensità)

x_hsi[:,:,2] = equalize_hist(x_hsi[:,:,2])

# riconverto per visualizzare con imshow

z = hsi2rgb(x_hsi)

plt.figure()
plt.subplot(1,3,1)
plt.title('Immagine originale')
plt.imshow(x, clim = [0,1])
plt.subplot(1,3,2)
plt.title('Equalizzazione in RGB')
plt.imshow(y1)
plt.subplot(1,3,3)
plt.title('Equalizzazione in HSI')
plt.imshow(z)

# con HSI preservo la tinta, mentre RGB modifica i colori
# in quanto applico una trasformazione diversa ad ognuna delle bande
# perchè diversa è la distribuzione dei livelli di grigio e quindi
# diversa sarà anche l'equalizzazione