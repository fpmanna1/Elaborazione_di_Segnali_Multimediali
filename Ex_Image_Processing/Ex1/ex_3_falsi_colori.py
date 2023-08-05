# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:22:09 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import skimage.io as io # importa il modulo Input/Output di SK-Image 

R = io.imread('Washington_red.tif') 
G = io.imread('Washington_green.tif') 
B = io.imread('Washington_blue.tif') 
I = io.imread('Washington_infrared.tif')

x = np.stack((R,G,B), 2) 
plt.figure(1); plt.imshow(x); plt.show();

y = np.stack((I,G,B), 2)
plt.figure(2); plt.imshow(y); plt.show();