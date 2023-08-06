# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:01:05 2023

@author: nokia
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

from skimage.transform import warp 

"""
Rotazione Centrale. Scrivete una funzione con il prototipo ruota(x, theta) 
che utilizza la funzione warp per ruotare di un’angolo theta l’immagine x 
rispetto al centro dell’immagine. A tal fine usarte una combinazione di 
traslazioni e rotazione. Ricordatevi che la combinazione di diverse 
trasformazioni affini `e ancora una trasformazione affine, che pu`o 
essere ottenuta tramite il prodotto (matriciale) delle
matrici che le definiscono.
"""

plt.close('all')


def ruota(x, theta): # l'input è in radianti
    
    M,N = x.shape
    
    A1 = np.array([[1,0,N/2],[0,1,M/2],[0,0,1]], dtype=np.float32) 
    # trasla nel punto centrale
    
    A2 = np.array([[np.cos(theta),np.sin(theta),0], [-np.sin(theta),np.cos(theta),0], [0,0,1]], dtype=np.float32)
    A3 = np.array([[1,0,-N/2],[0,1,-M/2],[0,0,1]], dtype=np.float32)
    
    A = A1 @ A2 @  A3  # effettua una moltiplicazione tra matrici
    y = warp(x, A, order = 1, cval=255)
    return y


x = np.float32(io.imread('lena.jpg')) 
y = ruota(x, 1.5) 

plt.subplot(1,2,1);
plt.imshow(x,clim=[0,255],cmap='gray'); plt.title('originale'); plt.subplot(1,2,2);
plt.imshow(y,clim=[0,255],cmap='gray'); plt.title('ruotata');