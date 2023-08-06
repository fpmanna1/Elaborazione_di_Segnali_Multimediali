# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 12:55:45 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi
from sklearn.cluster import k_means

plt.close('all')

x = np.float64(io.imread('yeast.tif')) 
plt.figure(1); plt.imshow(x,clim=[0,255],cmap='gray'); plt.title('immagine originale');

# thresholding adattativo 
def thresholding_locale(x): 
    m_g = np.mean(x) 
    s_l = ndi.generic_filter(x, np.std, (3,3)) 
    mask = (x>30*s_l) & (x>1.5*m_g) 
    return mask

mapp = thresholding_locale(x) 
plt.figure(2); plt.imshow(mapp,clim=[0,1],cmap='gray');
plt.title('thresholding adattativo');