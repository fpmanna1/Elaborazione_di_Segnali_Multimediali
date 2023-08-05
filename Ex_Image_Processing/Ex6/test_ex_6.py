# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 17:38:36 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

plt.close('all')

"""
Filtraggio notch. L’immagine anelli.tif mostra una parte degli anelli 
che circondano Saturno. Il rumore sinusoidale `e dovuto ad un segnale AC 
sovrapposto a quello della fotocamera prima di digitalizzare l’immagine. 
Tale interferenza `e semplice da rimuovere se si progetta un filtro notch i
n grado di cancellare il contributo del rumore. Calcolate quindi 
la trasformata di Fourier dell’immagine, analizzatela, individuate
il contributo realtivo al segnale sinusoidale e cercate di eliminarlo
con il filtraggio.
"""

x = np.float32(io.imread('anelli.tif'))

plt.figure()
plt.title('Immagine originale')
plt.imshow(x, clim = [0,255], cmap = 'gray')


X = np.fft.fft2(x)
X = np.fft.fftshift(X)

plt.figure()
plt.title('Spettro Rumoroso')
plt.imshow(np.log(1+np.abs(X)), clim = None, cmap = 'gray', extent = (-0.5,+0.5,+0.5,-0.5))

M,N = x.shape
m = np.fft.fftshift(np.fft.fftfreq(M))
n = np.fft.fftshift(np.fft.fftfreq(N))

l,k = np.meshgrid(n,m)

H1 = 1-((k<-0.02) & (l > -0.01) & (l < 0.01))
H2 = 1-((k>0.02) & (l>-0.01) & (l < 0.01))

H = H1 & H2

Y = X * H

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))

plt.figure()
plt.title('Spettro ripulito')
plt.imshow(np.abs(Y), clim = None, cmap = 'gray', extent = (-0.5,0.5,0.5,-0.5))

plt.figure()
plt.title('Immagine ripulita')
plt.imshow(y, clim = [0,255], cmap = 'gray')








