# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:42:32 2023

@author: plett
"""

import skimage.data as data
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

from skimage.feature import local_binary_pattern

plt.close('all')

"""

# calcoliamo l'istogramma normalizzato delle descrizioni locali LBP
# per tre differenti tessiture

R =  1; P = 8; method = 'uniform'; # settings per LBP
# P: vicini che tengo in considerazione
# R: raggio del cerchio (considero vicini circolari)

def extract_feature(x):
    y = local_binary_pattern(x, P,R, method=method)
    feat, bins = np.histogram(y.flatten(),
                              bins = np.arange(0, np.max(y)+2), density=True)
    
    # flatten = ottiene un array monodimensionale a partire da
    # array multidimensionali
    
    # arange = crea un vettore composto automaticamente con una serie numerica
    # di default lo step è 1
    
    return feat

img_brick = np.float64(io.imread('Immagini/brick.png')) 
img_grass = np.float64(io.imread('Immagini/grass.png')) 
img_gravel = np.float64(io.imread('Immagini/gravel.png'))

# visualizzo istogrammi delle 3 tessiture

plt.figure()
plt.subplot(1,3,1)
plt.title('Brick')
plt.imshow(img_brick, clim = [0,255], cmap = 'gray')
plt.subplot(1,3,2)
plt.title('Grass')
plt.imshow(img_grass, clim = [0,255], cmap = 'gray')
plt.subplot(1,3,3)
plt.title('Gravel')
plt.imshow(img_gravel, clim = [0,255], cmap = 'gray')

feat_brick = extract_feature(img_brick) 
feat_grass = extract_feature(img_grass)
feat_gravel = extract_feature(img_gravel)


# valuto l'istogramma normalizzato LBP per l'immagine img1 e lo confronto
# con gli istogrammi ottenuti precedentemente
x = np.float64(io.imread('Immagini/img1.jpg')) 
feat = extract_feature(x) 
dist_brick = np.sum(np.abs(feat_brick -feat)) 
dist_grass = np.sum(np.abs(feat_grass -feat))
dist_gravel = np.sum(np.abs(feat_gravel-feat))

# si nota come il valore minimo lo abbiamo in corrispondenza dell'immagine grass
# infatti è la più simile a img1

plt.figure()
plt.subplot(1,4,1)
plt.title('Istogramma LBP brick')
plt.bar(np.arange(10), feat_brick)
plt.subplot(1,4,2)
plt.title('Istogramma LBP grass')
plt.bar(np.arange(10), feat_grass)
plt.subplot(1,4,3)
plt.title('Istogramma LBP gravel')
plt.bar(np.arange(10), feat_gravel)
plt.subplot(1,4,4)
plt.title('Istogramma img1')
plt.bar(np.arange(10), feat)


if dist_brick<dist_grass and dist_brick<dist_gravel: 
    print('e un muro')
elif dist_grass<dist_brick and dist_grass<dist_gravel: 
    print('e un prato')
else:
    print('e una ghiaia')
    
"""

# provo ad applicare k_means all'immagine LBP uniform (con 10 classi)


# calcolo immagine LBP

from sklearn.cluster import k_means

x = np.float32(io.imread('Immagini/brick.png'))

P = 8
R = 1

y = local_binary_pattern(x, P, R, method = 'uniform')

plt.figure()
plt.imshow(y, clim = [0, 9], cmap = 'gray')

# applico k_means

M,N = y.shape
D = np.reshape(y, (M*N,1))

K = 4

centroidi, label, mse = k_means(D,K)

label = np.reshape(label, (M,N))

plt.figure()
plt.imshow(label, clim = [0,K-1], cmap = 'jet', interpolation = 'bicubic')




