# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:20:20 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import skimage.io as io # importa il modulo Input/Output di SK-Image 
from os.path import isfile

plt.close('all')

x = io.imread("dorian.jpg")
y = io.imread("granelli.jpg")

plt.figure(1)
plt.imshow(y, clim = [0,255] , cmap = 'gray') 

plt.figure(2)
plt.imshow(y, clim = None, cmap = 'gray')

# fa un FSHS, ma solo in fase di visualizzazione, senza
# cambiare i valori dei pixel
