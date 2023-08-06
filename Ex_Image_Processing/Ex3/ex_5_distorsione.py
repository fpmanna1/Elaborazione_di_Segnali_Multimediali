# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:27:36 2023

@author: nokia
"""

'''
Distorsione. 
Scrivete la funzione che realizza la distorsione di un’immagine 
lungo la direzione verticale e orizzontale e che abbia il prototipo: 
    deforma(x,c,d). 
    Scegliete un’immagine e al variare dei parametri
c e d osservate il tipo di distorsione.
'''

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

from skimage.transform import warp 

plt.close('all')

def deforma(x, c, d):
    '''
        funzione per deformare un'immagine x: c e d sono i parametri
        da dare rispettivamente per la deformazione verticale e orizzontale
    '''
    M = x.shape[0] 
    N = x.shape[1]
    
    
    A_ver = np.array([ [1,0,0], [c,1,0], [0,0,1]], dtype=np.float32)
    A_ori = np.array([ [1,d,0], [0,1,0], [0,0,1]], dtype=np.float32)
    
    A = np.multiply(A_ver, A_ori) # applico entrambe le distorsioni
    # A = A1 @ A2
    #A_def = A[[1,0,2],:][:,[1,0,2]].T
    A_def = A
    
    y4 = warp(x, A_ori, output_shape=(2*M,2*N), order = 3)
    
    return y4
    

x = np.float32(io.imread('lena.jpg'))
y = deforma(x, 0.3, 0.2)

plt.imshow(y,clim=[0,255],cmap='gray')
