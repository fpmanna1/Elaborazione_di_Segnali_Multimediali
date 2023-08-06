# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 12:51:09 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from sklearn.cluster import k_means

plt.close('all')

x = np.float32(io.imread('Fiori256.bmp'))/255

M,N,C = x.shape

K = 4

d = np.reshape(x, (M*N, C))
centroidi, idx, mse = k_means(d,K)
idx = np.reshape(idx, (M,N))

plt.imshow(idx, clim = [0,K-1], cmap= 'jet')

