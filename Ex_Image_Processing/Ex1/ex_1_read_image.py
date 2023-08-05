# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:58:02 2023

@author: nokia
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import skimage.io as io # importa il modulo Input/Output di SK-Image 
from os.path import isfile

nomefile = "lena.jpg"
nomefile2 = "house.y"

def vediJPG(nomefile): 
    
    """
    carica un’immagine memorizzata in formato JPEG e la visualizza.
    x = vediJPG(nomefile) carica l’immagine contenuta nel file ’nomefile’ 
    """
    
    if not isfile(nomefile): 
        print('Il file %s non esiste!' % nomefile)
    else: 
        x = io.imread(nomefile) 
        x = np.float32(x) 
        plt.figure()
        plt.imshow(x, clim=(0,255), cmap='gray') 
        plt.show()
    return x

def vediRAW(nomefile,M,N,dtype): 
    """
    carica un’immagine in formato grezzo e la visualizza. 
    x = vediRAW(nomefile,M,N,dtype) carica l’immagine di dimensioni MxN contenuta in ’nomefile’;
    tipo e’ il formato di dato (np.uint8, np.float32, ecc.) 
    """
    if not isfile(nomefile): 
        print('Il file %s non esiste!' % nomefile)
    else: 
        x = np.fromfile(nomefile, dtype) 
        x = np.reshape(x, (M, N)) # reshape permette di ottenere la matrice 
        x = np.float32(x) 
        plt.figure(); plt.imshow(x, clim=(0,255), cmap='gray') 
        plt.show()
    return x


#vediJPG(nomefile)
vediRAW(nomefile2, 512, 512, np.uint8)
