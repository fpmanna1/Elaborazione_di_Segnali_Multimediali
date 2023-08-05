# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:52:04 2023

@author: plett
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

plt.close('all')

x = np.float64(io.imread('granelli.jpg'))
y = np.float64(io.imread('vista_aerea.jpg'))

plt.figure(1)
plt.subplot(1,2,1)
plt.title('granelli originale')
plt.imshow(x, clim = [0,255], cmap = 'gray')

plt.subplot(1,2,2)
plt.title('vista_aerea originale')
plt.imshow(y, clim= [0,255], cmap = 'gray')


# istogramma immagine aerea originale

h, b = np.histogram(x, np.arange(257))
plt.figure(2)
plt.title('istogramma immagine aerea originale')
plt.bar(np.arange(256), h)



# effettuiamo le trasformazioni

# dato che sono entrambe sovraesposte, riduciamo la 
# luminosità media

b = 50
x = x - b
y = y - b
# poichè sottraggo -b, potrei avere valori negativi
# definisco una maschera che mette a 0 tali valori
 
mask = x < 0 # creo una matrice di vero e falso
x[mask] = 0 # si annullano tutti i valori minori di zero

mask_y = y < 0
y[mask_y] = 0

print(mask)
print(mask_y)

plt.figure(3)
plt.subplot(1,2,1)
plt.title('granelli modificata')
plt.imshow(x, clim = [0,255], cmap = 'gray')

plt.subplot(1,2,2)
plt.title('vista_aerea modificata')
plt.imshow(y, clim = [0,255], cmap = 'gray')

h_mod, b_mod = np.histogram(x, np.arange(257))
plt.figure(4)
plt.title('istogramma immagine aerea modificata')
plt.bar(np.arange(256), h_mod)