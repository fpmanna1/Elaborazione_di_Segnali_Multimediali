# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:16:21 2023

@author: nokia
"""
import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

from skimage.transform import warp 

plt.close('all')

x = np.float32(io.imread('lena.jpg')) 
x = x[252:277,240:290]; M = x.shape[0]; N = x.shape[1]

plt.figure(1)
plt.imshow(x, clim = [0,255], cmap='gray')

A = np.array([ [0.5,0,0], [0,0.5,0], [0,0,1]], dtype=np.float32) 
y1 = warp(x, A, output_shape=(2*M,2*N), order = 0) 
y2 = warp(x, A, output_shape=(2*M,2*N), order = 1) 
y3 = warp(x, A, output_shape=(2*M,2*N), order = 3)

plt.figure(2)
plt.subplot(3,1,1);
plt.imshow(y1,clim=[0,255],cmap='gray'); plt.title('interpolazione nearest'); plt.subplot(3,1,2);
plt.imshow(y2,clim=[0,255],cmap='gray'); plt.title('interpolazione bilinear'); plt.subplot(3,1,3);
plt.imshow(y3,clim=[0,255],cmap='gray'); plt.title('interpolazione bicubic');