# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:58:00 2023

@author: plett
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io

plt.close('all')

x = io.imread('fragole.jpg') 
x = np.float64(x)/255 

y = 1 - x

plt.subplot(1,2,1); 
plt.imshow(x); 
plt.title('Immagine Originale'); 
plt.subplot(1,2,2); 
plt.imshow(y); 
plt.title('Immagine Negata');