# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 12:18:43 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from sklearn.cluster import k_means

plt.close('all')

x = io.imread('dowels.tif')

# creo una matrice con un numero di righe pari ai pixel dell'immagine
# e numero di colonne pari al numero di informazioni da associare
# ad ogni pixel (in questo caso è solo l'intensità luminosa)

M,N = x.shape
Nc = 3

d = np.reshape(x, (M*N,1))

# idx = ad ogni pixel, a che regione l'ho associato
# mse = errore di approssimare al proprio valore il centroide
# errore tra quel valore e il centroide
# è un indice utile per capire se il clustering è andato bene o meno

centroidi, idx, mse = k_means(d, Nc)

idx = np.reshape(idx, (M, N))

plt.figure()
plt.imshow(idx, clim = [0,Nc-1], cmap = 'jet', interpolation='nearest')

