

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

from color_convertion import rgb2hsi, hsi2rgb

plt.close('all')

# voglio sfocare Lena con un filtro passa-basso in frequenza

x = np.float32(io.imread('lena.jpg'))

# calcolare la tdf
# vedere spettro e fase
# fare filtraggio
# visualizzare l'immagine

X = np.fft.fftshift(np.fft.fft2(x))

M,N = x.shape
m = np.fft.fftshift(np.fft.fftfreq(M))
n = np.fft.fftshift(np.fft.fftfreq(N))

l,k = np.meshgrid(n,m)

# definisco il filtro

b = 0.07
D = np.sqrt(k**2 + l**2) 

H = np.exp(-D**2/(2*(b**2)))

plt.figure()
plt.title('Maschera del filtro')
plt.imshow(H, clim = [0,1], cmap = 'gray')

Y = X * H

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))

plt.figure()
plt.subplot(1,2,1)
plt.title('Immagine originale')
plt.imshow(x, clim = [0,255], cmap = 'gray')
plt.subplot(1,2,2)
plt.title('Immagine sfocata')
plt.imshow(y, clim = [0,255], cmap = 'gray')






