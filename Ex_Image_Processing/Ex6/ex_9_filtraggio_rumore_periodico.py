# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:34:44 2023

@author: plett
"""

import numpy as np # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib 
import scipy.ndimage as ndi # importa Scipy per le immagini 
import skimage.io as io # importa il modulo Input/Output di SK-Image

plt.close('all')

x = np.fromfile('lenarumorosa.y', np.int16)
x = np.reshape(x, [512, 512])
x = np.float64(x)

plt.figure()
plt.imshow(x, clim = [0,255], cmap = 'gray')
plt.title('Immagine rumorosa')

X = np.fft.fftshift(np.fft.fft2(x))
plt.figure()
plt.imshow(np.log(1+np.abs(X)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5));
plt.title('Trasformata di Fourier di un immagine rumorosa')

# vogliamo rimuovere solo la parte dello spettro relativa alla sinusoide
"""
Notate che teoricamente la sinusoide dovrebbe essere rappresentata da due impulsi 
in frequenza. Nella pratica non abbiamo degli impulsi ideali, bensì due sinc. 
Questo `e dovuto al fatto che il rumore sinusoidale aggiunto
`e limitato all’immagine, cio`e risulta troncato nello spazio lungo le 
due direzioni attraverso una finestra rettangolare bidimensionale. 
Il prodotto tra la sinusoide e la finestra in frequenza `e la 
convoluzione tra i due impulsi e la sinc bidimensionale (trasformata dell’impulso rettangolare), 
quindi due sinc localizzate proprio alle
frequenze specificate dalla sinusoide
"""

# Definizione del filtro 

nu = 0.2; B = 0.03
m = np.fft.fftshift(np.fft.fftfreq(X.shape[0])) 
n = np.fft.fftshift(np.fft.fftfreq(X.shape[1])) 
l,k = np.meshgrid(n,m) 
D1 = np.sqrt(k**2+(l-nu)**2) 
D2 = np.sqrt(k**2+(l+nu)**2) 
H = (D1>B) & (D2>B)

plt.figure(); plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5)); 
plt.title('Risposta in frequenza del filtro');

# Filtraggio 
Y = X * H; plt.figure();
plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5)); 
plt.title('Trasformata di Fourier immagine filtrata');
y = np.real(np.fft.ifft2(np.fft.ifftshift(Y))); plt.figure(); plt.imshow(y, clim=[0,256], cmap='gray'); 
plt.title('Immagine filtrata');

# Calcolo MSE 
xo = np.fromfile('lena.y', np.uint8) 
xo = np.reshape(xo, [512,512]) 
xo = np.float64(xo)
plt.figure(); plt.imshow(xo, clim=[0,256], cmap='gray'); plt.title('immagine originale');
MSE = np.mean((xo-y) ** 2)

"""
In realt`a, con questo filtro non si riescono a rimuovere perfettamente le 
righe verticale, a causa della presenza dei lobi laterali, che presentano 
valori non trascurabili. E’ possibile progettare un filtro rettangolare 
molto stretto che (conservando i valori intorno all’origine che  
                   corrispondono al contenuto frequenziale rilevante del
segnale) sia diretto proprio lungo l’asse orizzonta
"""

# Definizione del filtro 
Bk = 0.004; Bl = 0.02;
H1 = (-Bk <= k) & (k <= Bk) 
H2 = (-Bl <= l) & (l <= Bl) 
H = (~H1) | (H2 & H1) 
plt.figure(); plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5)); 
plt.title('Risposta in frequenza del filtro');
Y = X * H 
y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)));
plt.figure(); plt.imshow(y, clim=[0,256], cmap='gray'); plt.title('Immagine filtrata');
MSE = np.mean((xo-y) ** 2)

xo = np.fromfile('lena.y', np.uint8) 
xo = np.reshape(xo, [512,512]) 
xo = np.float64(xo)
plt.figure(); plt.imshow(xo, clim=[0,256], cmap='gray'); plt.title('immagine originale');

"""
# VERSIONE ALTERNATIVA

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io

plt.close('all')

# esercizio filtraggio rumore periodico

x = np.fromfile('lenarumorosa.y', np.int16)
x = np.reshape(x, (512,512))

plt.figure()
plt.imshow(x, clim = [0,255], cmap = 'gray')

X = np.fft.fftshift(np.fft.fft2(x))

Z = np.log(1+np.abs(X))

plt.figure()
plt.title('Modulo rumorosa')
plt.imshow(Z, clim = None, cmap = 'gray', extent = (-0.5,+0.5,+0.5,-0.5))

# definizione del filtro

M,N = x.shape
m = np.fft.fftshift(np.fft.fftfreq((M)))
n = np.fft.fftshift(np.fft.fftfreq((N)))

l,k = np.meshgrid(n,m)

H1 = (k>-0.02) & (k<0.02) & (l < -0.10)
H2 = (k>-0.02) & (k<0.02) & (l > 0.1) 

H = (1-H1) & (1-H2)

plt.figure()
plt.title('Maschera del filtro')
plt.imshow(H, clim = None, cmap = 'gray', extent = (-0.5,+0.5,+0.5,-0.5))

Y = X * H

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))

plt.figure()
plt.title('Immagine senza rumore')
plt.imshow(y, clim = [0,255], cmap = 'gray')


"""