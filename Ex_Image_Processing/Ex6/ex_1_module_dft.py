# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:55:16 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = np.float32(io.imread('lena.jpg'))
X = np.fft.fft2(x) # calcola la dft su MxN punti, valore di default

plt.figure(1)
plt.imshow(x, clim = [0,255],cmap='gray')


# visualizziamo il modulo della dft, dopo aver fatto lo shift per portare le basse frequenze
# intorno allo zero e dopo aver applicato una trasformazione logaritmo
# che mi permette di visualizzare meglio le alte frequenze

Y = np.log(1+np.abs(np.fft.fftshift(X))) 

plt.figure(2)
plt.imshow(Y, clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));

# un altro modo per visualizzare il modulo della tdf è attraverso
# un grafico 3d

Y = np.log(1+np.abs((np.fft.fftshift(X)))) 
m = np.fft.fftshift(np.fft.fftfreq(Y.shape[0])) 
n = np.fft.fftshift(np.fft.fftfreq(Y.shape[1]))

from mpl_toolkits.mplot3d import Axes3D 

ax = Axes3D(plt.figure()); # crea una figura per i grafici 3d
l,k = np.meshgrid(n,m)
ax.plot_surface(l,k,Y, linewidth=0, cmap='jet')

