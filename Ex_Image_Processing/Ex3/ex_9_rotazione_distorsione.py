# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:08:16 2023

@author: nokia
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image
import skimage

from skimage.transform import warp 

plt.close('all')

"""
Combinazione di operazioni geometriche. Scrivete una funzione dal prototipo
 rot shear(x,theta,c) per realizzare una rotazione e poi una distorsione 
 verticale (attenzione all’ordine!). Fate le due operazioni rispetto al 
 centro dell’immagine. Create l’immagine di ingresso usando il seguente 
 comando x = np.float64(skimage.data.checkerboard()) in modo da generare 
 una scacchiera su cui le modifiche
risultano essere pi`u facilmente visibili.
"""


def rot_shear(x, theta, c): 
    M,N = x.shape
    T1 = np.array([[1,0,0],[0,1,0],[M/2,N/2,1]], dtype=np.float32) # traslazione
    T2 = np.array([[np.cos(theta),np.sin(theta),0], [-np.sin(theta),np.cos(theta),0], [0,0,1]], dtype=np.float32) # rotazione
    T3 = np.array([[1,0,0],[c,1,0],[0,0,1]], dtype=np.float32) # deformazione verticale
    T4 = np.array([[1,0,0],[0,1,0],[-M/2,-N/2,1]], dtype=np.float32) # traslazione
    
    T = T4 @ T3 @ T2 @ T1 # faccio i prodotti matriciali all'incontrario
    A = T[[1,0,2],:][:,[1,0,2]].T  # passaggio dalla matrice della teoria a quella di Python
    y = warp(x, A, order = 1)
    return y



x = np.float64(skimage.data.checkerboard()) # crea una scacchiera per vedere meglio le modifiche

y = rot_shear(x, 0.3, 0.3)

plt.subplot(1,2,1);
plt.imshow(x,clim=[0,255],cmap='gray'); plt.title('originale'); plt.subplot(1,2,2);
plt.imshow(y,clim=[0,255],cmap='gray'); plt.title('rotazione + distorsione verticale');