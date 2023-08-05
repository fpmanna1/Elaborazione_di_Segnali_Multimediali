# -*- coding: utf-8 -*-
"""
Created on Mon May 15 18:15:52 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = np.float32(io.imread('spettro.jpg'))

plt.figure(1)
plt.title('spettro originale')
plt.imshow(x, clim=[0,255], cmap = 'gray')

# l'immagine è caratterizzata da una dinamica molto elevata
# con un'operazione log diminuisco la dinamica dei valori più luminosi
# i valori più scuri risentono meno dell'operazione
# i coeff. alle alte frequenze, essendo molto piccoli
# difficilmente vengono visualizzati

# applico l'operazione logaritmo

x = np.log(x+1)

# successivamente applico il fshs (solo in fase di visualizzazione)

plt.figure(2)
plt.title('spettro dopo op. log e fshs')
plt.imshow(x, clim = None, cmap = 'gray')