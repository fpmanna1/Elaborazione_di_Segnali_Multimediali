# -*- coding: utf-8 -*-
"""
Created on Sat May 13 13:52:41 2023

@author: plett
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

plt.close('all')

x = io.imread('fragole.jpg')
plt.figure(1)
plt.imshow(x)

# isoliamo le 3 componenti RGB

R = x[:, :, 0]
plt.figure(2)
plt.title('Componente di rosso')
plt.imshow(R, cmap='gray', clim = [0,255])

G = x[:,:,1]
plt.figure(3)
plt.title('Componente di verde')
plt.imshow(G, cmap='gray', clim=[0,255])

B = x[:,:,2]
plt.figure(4)
plt.title('Componente di blu')
plt.imshow(B, cmap='gray', clim = [0,255])

# i valori più luminosi si ottengono in corrispondenza
# delle componente di colore che sono presenti maggiormente
# nell'immagine