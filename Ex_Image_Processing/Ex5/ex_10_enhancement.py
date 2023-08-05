# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 12:58:57 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
import skimage

from skimage.exposure import equalize_hist
from skimage.transform import warp
from color_convertion import rgb2hsi, hsi2rgb
from skimage.color import rgb2yuv, yuv2rgb 

plt.close('all')

"""
Enhancement. Si vuole realizzare l’enhancement dell’immagine a colori 
primopiano.jpg allo scopo di migliorarne sia la luminosit`a che il contrasto. 
Scrivete il codice python in cui effettuate tutte le operazioni che ritenete 
necessarie (giustificando le scelte) sia nello spazio RGB che in quello HSI 
e stabilite qual `e lo spazio pi`u conveniente in cui lavorare. Infine, 
ruotate l’immagine in modo che le linee che si intravedono
nello sfondo risultino perfettamente orizzontali.
"""

x = np.float32(io.imread('primopiano.jpg'))/255

# ENHANCEMENT IN RGB

#y = x + 45/255
y_rgb = x * 1.7 + 45/255
#y = x ** 0.5
# un fattore a > 1 tende a migliorare il contrasto (espandendo la dinamica)


# ENHANCEMENT IN HSI

x_hsi = rgb2hsi(x)

# estrazione bande tinta, saturazione ed intensità
H = x_hsi[:,:,0]
S = x_hsi[:,:,1]
I = x_hsi[:,:,2]

x_hsi[:,:,2] = I**0.6

y_hsi = hsi2rgb(x_hsi)

# rotazione dell'immagine di un angolo di 0.3 radianti

# definisco la matrice della trasformazione

def ruota(x, angle):
    M,N,Y = x.shape
    
    T1 = np.array([[1,0,0],[0,1,0],[M/2, N/2, 1]], dtype = np.float32) # traslo rispetto al centro dell'immagine
    T2 = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0,0,1]], dtype = np.float32) # ruoto
    T3 = np.array([[1,0,0],[0,1,0],[-M/2, -N/2, 1]], dtype = np.float32) # ritraslo
    
    
    A1 = T1[[1,0,2],:][:,[1,0,2]].T
    A2 = T2[[1,0,2],:][:,[1,0,2]].T
    A3 = T3[[1,0,2],:][:,[1,0,2]].T
    

    A = A1 @ A2 @ A3
    
    y = warp(x, A, order = 1)
    
    return y
    
y_def = ruota(y_hsi, -0.3)


plt.figure()
plt.subplot(1,3,1)
plt.title('Immagine originale')
plt.imshow(x)
plt.subplot(1,3,2)
plt.title('Enhancement RGB')
plt.imshow(y_rgb)
plt.subplot(1,3,3)
plt.title('Enhancement in HSI')
plt.imshow(y_def)
