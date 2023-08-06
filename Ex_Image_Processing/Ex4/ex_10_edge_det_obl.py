# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:05:19 2023

@author: plett
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

# queste maschere danno più importanza ai bordi nella direzione obliqua
# andiamo a fare edge detection

x = np.float64(io.imread('angiogramma.jpg'))

x = ndi.gaussian_filter(x, (1,1))

# definisco le maschere

m1 = [[0,1,2], [-1,0,1], [-2,-1, 0]]
m2 = [[-2,-1,0], [-1,0,1], [0,1,2]]

y1 = ndi.correlate(x, m1)
y2 = ndi.correlate(x, m2)
grad = np.abs(y1) + np.abs(y2)

y_grad = ndi.gaussian_filter(grad, (1,1))

plt.figure()
plt.subplot(1,3,1)
plt.title('Immagine originale')
plt.imshow(x, clim = [0,255], cmap = 'gray')
plt.subplot(1,3,2)
plt.title('Gradiente')
plt.imshow(grad, clim = [0,255], cmap='gray')
plt.subplot(1,3,3)
plt.title('Gradiente con filtro gaussiano')
plt.imshow(y_grad, clim = [0,255], cmap='gray')