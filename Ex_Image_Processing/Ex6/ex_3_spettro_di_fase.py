# -*- coding: utf-8 -*-
"""
Created on Tue May 16 18:39:53 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = np.float64(io.imread('volto.tif')) 

plt.figure(1)
plt.title('immagine originale')
plt.imshow(x, clim = [0,255], cmap = 'gray')

X = np.fft.fft2(x) 
Xf = np.fft.fftshift(X) 
plt.figure(2) 
Z = np.log(1+np.abs(Xf)); # enhancement per visualizzazione 
plt.subplot(1,2,1);
plt.imshow(Z,clim=None,cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))
plt.title('Spettro di ampiezza')
plt.subplot(122)
plt.imshow(np.angle(Xf), clim=[-np.pi, np.pi], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Spettro di fase');

# Proviamo adesso a ricostruire un’immagine con la sola 
# informazione di ampiezza o con la sola informazione di fase

ym = np.real(np.fft.ifft2(np.abs(X))) # ricostruzione solo modulo
yf = np.real(np.fft.ifft2(np.exp(1j*np.angle(X)))) # ricostruzione solo fase 
plt.figure(3) 

z = np.log(ym-np.min(ym)+1); # enhancement per la visualizzazione 
plt.subplot(1,2,1); plt.imshow(z, clim=None, cmap='gray')
plt.title('Ricostruzione spettro di ampiezza')
plt.subplot(1,2,2); plt.imshow(yf, clim=None, cmap='gray')
plt.title('Ricostruzione spettro di fase');

