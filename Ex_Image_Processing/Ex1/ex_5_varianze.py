# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:16:44 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import skimage.io as io # importa il modulo Input/Output di SK-Image 
import scipy.ndimage as ndi

plt.close('all')


def varianze(x, K): 
    """
    calcola l’immagine delle varianze 
    """
    M = x.shape[0] 
    N = x.shape[1] 
    VAR = np.zeros((M-K+1,N-K+1)) 
    for i in range(M-K+1): 
        for j in range(N-K+1): 
            VAR[i,j] = np.var(x[i:i+K,j:j+K])
    return VAR


def varianze_v2(x, K): 
    """
    calcola l’immagine delle varianze 
    """
    return ndi.generic_filter(x, np.var, (K,K))


nomefile = "dorian.jpg"
x = io.imread(nomefile) 
x = np.float32(x) 

plt.figure(1)
plt.imshow(x, clim=(0,255), cmap='gray')
plt.title("Immagine normale")

z = varianze_v2(x, 5)

plt.figure(2)
plt.imshow(z, clim=(0,255), cmap='gray')
plt.title("Varianze con k=3")
