# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:09:07 2023

@author: plett
"""

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

plt.close('all')

x = np.float64(io.imread('lena.jpg'))

M,N = x.shape 

# matrici delle frequenze orizzontali e verticali
m = np.fft.fftshift(np.fft.fftfreq(M)) # frequenze verticali
n = np.fft.fftshift(np.fft.fftfreq(N)) # frequenze orizzontali
l,k = np.meshgrid(n,m) # prima orizzontali poi verticali

D = np.sqrt(k**2+ l**2) 

D0 = 0.1; H = (D <= D0) 
# aumentando il raggio, lascio passare più frequenze, quindi
# l'immagine migliora
plt.figure();
plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));

X = np.fft.fft2(x) 
X = np.fft.fftshift(X)
plt.figure();
plt.imshow(np.log(1+np.abs(X)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
Y = H * X
plt.figure();
plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
Y = np.fft.ifftshift(Y) 
y = np.real(np.fft.ifft2(Y)) 
plt.figure();
plt.imshow(y, clim=[0,255], cmap='gray');