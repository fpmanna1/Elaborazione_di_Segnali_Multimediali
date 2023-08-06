# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 17:39:54 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = io.imread('filamento.jpg') 
plt.figure(1)
plt.imshow(x, clim=[0,255], cmap='gray');

MED = ndi.generic_filter(x, np.mean, (3,3)) # media locale
DEV = ndi.generic_filter(x, np.std , (3,3))  # dev locale

plt.figure(2)
plt.subplot(1,2,1)
plt.title('Medie Locali')
plt.imshow(MED, clim = [0,255], cmap = 'gray')
plt.subplot(1,2,2)
plt.title('Varianze locali')
plt.imshow(DEV, clim = [0,255], cmap = 'gray')

med = np.mean(x) # media globale
dev = np.std(x)  # dev globale

mask = (MED<=0.4*med) & (DEV<=0.4*dev) & (DEV>=0.02*dev) 
y = x + 3*x*mask # aumento la luminosità delle zone scure individuate dalla maschera
# se sono fuori dalla maschera, l'immagine resta invariata

plt.figure(3)
plt.imshow(y, clim=[0,255], cmap='gray');