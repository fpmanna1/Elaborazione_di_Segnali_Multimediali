# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 11:52:07 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
import skimage

from skimage.exposure import equalize_hist
from color_convertion import rgb2hsi, hsi2rgb
from skimage.color import rgb2yuv, yuv2rgb 

plt.close('all')


x = np.float64(io.imread('foto_originale.tif'))/255

plt.figure(1)
plt.title('Immagine originale')
plt.imshow(x)

# calcolo trasformata di Fourier
# definizione del filtro
# applico convoluzione col filtro
# vedo il risultato

# filtraggio nello spazio HSI 
w = rgb2hsi(x) 
I = w[:,:,2]
X = np.fft.fftshift(np.fft.fft2(I)) 
m = np.fft.fftshift(np.fft.fftfreq(X.shape[0])) 
n = np.fft.fftshift(np.fft.fftfreq(X.shape[1])) 

l,k = np.meshgrid(n,m)

H = (np.abs(l)<=0.10) & (np.abs(k)<=0.25); 
Y = H * X

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y))) 
w[:,:,2] = y 
z = hsi2rgb(w)

plt.figure(2); plt.imshow(z);
plt.title('Immagine filtrata');

plt.figure(3)
plt.imshow(H, clim = [0,1], cmap = 'gray')
