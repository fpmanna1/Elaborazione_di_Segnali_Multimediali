# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 18:26:11 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

plt.close('all')

x = np.float64(io.imread('car.tif')) 

M,N = x.shape

plt.figure(1); plt.imshow(x, clim=[0,255], cmap='gray'); plt.title('immagine originale');

X = np.fft.fftshift(np.fft.fft2(x)) 
plt.figure(2);
plt.imshow(np.log(1+np.abs(X)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5)); plt.title('Trasformata di Fourier immagine originale');
# Definizione del filtro 
mu_1 = 0.15; nu_1 = +0.18; B_1 = 0.023; mu_2 = 0.17; nu_2 = -0.16; B_2 = 0.023; mu_3 = 0.32; nu_3 = +0.18; B_3 = 0.015; mu_4 = 0.34; nu_4 = -0.16; B_4 = 0.015;

m = np.fft.fftshift(np.fft.fftfreq(X.shape[0])) 
n = np.fft.fftshift(np.fft.fftfreq(X.shape[1])) 
l,k = np.meshgrid(n,m) 
H_1a = np.sqrt((k-mu_1)**2+(l-nu_1)**2) <= B_1 
H_1b = np.sqrt((k+mu_1)**2+(l+nu_1)**2) <= B_1 
H_2a = np.sqrt((k-mu_2)**2+(l-nu_2)**2) <= B_2 
H_2b = np.sqrt((k+mu_2)**2+(l+nu_2)**2) <= B_2 
H_3a = np.sqrt((k-mu_3)**2+(l-nu_3)**2) <= B_3 
H_3b = np.sqrt((k+mu_3)**2+(l+nu_3)**2) <= B_3 
H_4a = np.sqrt((k-mu_4)**2+(l-nu_4)**2) <= B_4 
H_4b = np.sqrt((k+mu_4)**2+(l+nu_4)**2) <= B_4 

H = ~(H_1a|H_1b|H_2a|H_2b|H_3a|H_3b|H_4a|H_4b)
 
plt.figure(3); plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5)); plt.title('Risposta in frequenza del filtro');

Y = X * H 
plt.figure(4);
plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5)); plt.title('Trasformata di Fourier immagine filtrata');

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y))) 
plt.figure(5); plt.imshow(y, clim=[0,255], cmap='gray'); plt.title('Immagine filtrata');
