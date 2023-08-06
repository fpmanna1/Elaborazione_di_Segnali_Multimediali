# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 16:48:36 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

plt.close('all')

x = np.float64(io.imread('anelli.tif'))
plt.figure(1); plt.imshow(x, clim=[0,255], cmap='gray'); plt.title('immagine originale');

M,N = x.shape
X = np.fft.fftshift(np.fft.fft2(x))
plt.figure(2);
plt.imshow(np.log(1+np.abs(X)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Trasformata di Fourier immagine rumorosa');

# Definizione del filtro
Bl = 0.004; Bk = 0.02;

m = np.fft.fftshift(np.fft.fftfreq(X.shape[0])) 
n = np.fft.fftshift(np.fft.fftfreq(X.shape[1])) 
l,k = np.meshgrid(n,m) 

H1 = (-Bl <= l) & (l <= Bl) 
H2 = (-Bk <= k) & (k <= Bk) 
H = (~H1) | (H2 & H1) 

plt.figure(3); plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Risposta in frequenza del filtro');


# Filtraggio 

Y = X * H

plt.figure(4);
plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5)); plt.title('Trasformata di Fourier immagine filtrata');

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y))) 
plt.figure(5); plt.imshow(y, clim=[0,255], cmap='gray'); plt.title('Immagine filtrata');
noise = y - x; plt.figure(6); plt.imshow(noise, clim=None, cmap='gray');
plt.title('Rumore eliminato');

# CODICE ALTERNATIVO
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

plt.close('all')

"""
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

"""