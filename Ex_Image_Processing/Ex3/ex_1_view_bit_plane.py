# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:06:45 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

from bitop import bitget 

plt.close('all')

x = io.imread('filamento.jpg') 

M, N = x.shape 
bitplane = np.zeros((M,N,8), dtype=np.bool) # matrice 3D 

for i in range(8): 
    bitplane[:,:,i] = bitget(x, i) 
    plt.figure()
    plt.subplot(2,4,i+1) 
    plt.imshow(bitplane[:,:,i], clim=[0,1], cmap='gray')
    plt.title('Bitplane %d' % i)