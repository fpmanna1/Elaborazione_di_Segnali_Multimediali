# -*- coding: utf-8 -*-
"""
Created on Mon May 15 21:23:45 2023

@author: plett
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

plt.close('all')

x = np.float32(io.imread('luna.jpg'))

plt.figure(1)
plt.title('immagine originale')
plt.imshow(x, clim = [0,255], cmap = 'gray')

mask = [[0,1,0],[1,-4,1],[0,1,0]]

y = ndi.correlate(x, mask)

plt.figure(2)
plt.title('laplaciano')
plt.imshow(y, clim = None, cmap = 'gray')
# ho applicato il fshs per vedere meglio l'immagine

# ora faccio immagine originale - laplaciano

mask_laplaciano = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], dtype=np.float64) 
z = ndi.correlate(x, mask_laplaciano)

# ho sfruttato il fatto che il filtro con tutti 0 e solo 1 al centro è l'immagine stessa
# dunque, sommandola al laplaciano, essendo un operatore lineare, ottengo
# il risultato desiderato
# faccio questa operazione per enfatizzare i dettagli dell'immagine

plt.figure(3)
plt.title('Immagine iniziale - laplaciano')
plt.imshow(z, clim = [0,255], cmap = 'gray')

# si nota come i dettagli risultino più definiti, vengono enfatizzati