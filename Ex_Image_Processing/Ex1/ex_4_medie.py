# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:44:43 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import skimage.io as io # importa il modulo Input/Output di SK-Image 
import scipy.ndimage as ndi

plt.close('all')

def medie(x, K): # immagine e dimensione blocco
    """
    calcola l’immagine delle medie 
    """
    
    M = x.shape[0] 
    N = x.shape[1] 
    MED = np.zeros((M-K+1,N-K+1)) 
    for i in range(M-K+1): 
        for j in range(N-K+1): 
            MED[i,j] = np.mean(x[i:i+K,j:j+K])
    return MED 

def medie_2(x, K):
    """ 
    calcola l’immagine delle medie 
    """
    MED = ndi.generic_filter(x, np.mean, (K,K), mode='constant')
    return MED

nomefile = "dorian.jpg"
x = io.imread(nomefile) 
x = np.float32(x) 



y_3 = medie_2(x, 3) # provare con 3,5,7,9
y_5 = medie_2(x, 5)
y_7 = medie_2(x, 7)
y_9 = medie_2(x, 9)

plt.subplot(5,1,1)
plt.imshow(x, clim=(0,255), cmap='gray')
plt.title("Immagine normale")

plt.subplot(5,1,2)
plt.imshow(y_3, clim=(0,255), cmap='gray') 
plt.title("k = 3")

plt.subplot(5,1,3)
plt.imshow(y_5, clim=(0, 255), cmap='gray')
plt.title("k = 5")

plt.subplot(5,1,4)
plt.imshow(y_7, clim=(0, 255), cmap='gray')
plt.title("k = 7")

plt.subplot(5,1,5)
plt.imshow(y_9, clim=(0, 255), cmap='gray')
plt.title("k = 9")

'''
plt.subplot(3,1,1)
plt.imshow(y1,clim=[0,255],cmap='gray')
plt.title('interpolazione nearest'); plt.subplot(3,1,2)
plt.imshow(y2,clim=[0,255],cmap='gray')
plt.title('interpolazione bilinear')
plt.subplot(3,1,3)
plt.imshow(y3,clim=[0,255],cmap='gray')
plt.title('interpolazione bicubic')
'''
