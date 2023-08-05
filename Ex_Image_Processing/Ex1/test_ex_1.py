# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:10:32 2023

@author: nokia
"""

import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi

plt.close('all')

x = io.imread('dorian.jpg')


h, b = np.histogram(x, np.arange(257))

plt.figure()
plt.bar(np.arange(256),h)
plt.axis([0,255,0,1.1*np.max(h)])

