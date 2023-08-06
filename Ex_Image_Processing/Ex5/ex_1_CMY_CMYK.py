# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:48:09 2023

@author: plett
"""

import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

def rgb2cmy(x):
    return 1.0 - x

x = io.imread('fragole.jpg') 
x = np.float64(x)/255 
z = rgb2cmy(x)

# dopo aver applicato la funzione rgb2cmy, ho ottenuto l'immagine
# di partenza nello spazio cmy
# per visualizzare i livelli di ciano, magenta e giallo,
# visualizzo una banda di colore alla volta

c = z[:,:,0] # Ciano 
m = z[:,:,1] # Magenta 
y = z[:,:,2] # Giallo

plt.figure();
plt.subplot(1,3,1); 
plt.imshow(c,clim=[0,1],cmap='gray'); 
plt.title('Ciano'); 
plt.subplot(1,3,2); 
plt.imshow(m,clim=[0,1],cmap='gray'); 
plt.title('Magenta');
plt.subplot(1,3,3);
plt.imshow(y,clim=[0,1],cmap='gray'); 
plt.title('Giallo');

# ciano, magenta e giallo lo posso vedere come
# quantità di inchiostro che io aggiungo sul foglio bianco
# per aggiungere il nero devo ottenere il max livello
# di ciano, magenta e giallo
 

from matplotlib.colors import ListedColormap 
L = np.arange(255,-1,-1)/255 
B = np.ones(256)

# 256 valori tra da 1 ad 0 # 256 valori unitary
cmap_c = ListedColormap(np.stack((L,B,B),-1)) # palette per il Ciano 
cmap_m = ListedColormap(np.stack((B,L,B),-1)) # palette per il Magenta 
cmap_y = ListedColormap(np.stack((B,B,L),-1)) # palette per il Giallo

plt.figure();
plt.subplot(1,3,1); 
plt.imshow(c,clim=[0,1],cmap=cmap_c); 
plt.title('Ciano'); 
plt.subplot(1,3,2); 
plt.imshow(m,clim=[0,1],cmap=cmap_m); 
plt.title('Magenta');
plt.subplot(1,3,3); 
plt.imshow(y,clim=[0,1],cmap=cmap_y); 
plt.title('Giallo');


# vediamo adesso lo spazio cmyk

def rgb2cmyk(x): 
    z = 1.0 - x # conversione in CMY
    
# da rgb a cmyk
    k = np.min(z,-1) # stima del Nero 
    c = z[:,:,0] - k # rimozione del Nero al Ciano
    m = z[:,:,1] - k # rimozione del Nero al Magenta 
    y = z[:,:,2] - k # rimozione del Nero al Giallo 
    return np.stack((c,m,y,k),-1)

z = rgb2cmyk(x) 
c = z[:,:,0] # Ciano 
m = z[:,:,1] # Magenta 
y = z[:,:,2] # Giallo 
k = z[:,:,3] # Nero

plt.figure(); 
L = np.arange(255,-1,-1)/255 
cmap_k = ListedColormap(np.stack((L,L,L),-1)) # palette per il Nero 
plt.subplot(1,4,1); 
plt.imshow(c,clim=[0,1],cmap=cmap_c); 
plt.title('Ciano'); 
plt.subplot(1,4,2); 
plt.imshow(m,clim=[0,1],cmap=cmap_m); 
plt.title('Magenta'); 
plt.subplot(1,4,3); 
plt.imshow(y,clim=[0,1],cmap=cmap_y); 
plt.title('Giallo');
plt.subplot(1,4,4);
plt.imshow(k,clim=[0,1],cmap=cmap_k); 
plt.title('Nero');

# il ciano, nella scala CMY, era solo utilizzato per creare il nero
# nello spazio CMYK, non uso proprio il ciano