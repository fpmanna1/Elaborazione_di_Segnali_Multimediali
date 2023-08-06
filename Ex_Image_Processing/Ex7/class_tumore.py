# -*- coding: utf-8 -*-
"""
Created on Mon May  1 18:18:18 2023

@author: plett
"""

import skimage.data as data
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import skimage.io as io


plt.close('all')

label = np.load('Immagini/train_label.npy')
feats = np.load('Immagini/train_lbp_8_1_default.npy')

# normalizzo per normalizzare in un certo senso i pesi (importanza) delle features

MU = np.mean(feats, 0)
STD = np.std(feats, 0)
# Mu e STD sono calcolate tra immagini diverse

feats_norm = (feats - MU) / (STD + 1e-15)
# aggiungo una quantità piccola per evitare divisoni per zero

from sklearn.svm import LinearSVC
# linear: perchè è un iperpiano

classificatore = LinearSVC(C=1, max_iter=1000).fit(feats_norm, label)

x = np.float64(io.imread('Immagini/test_breakhis.png'))
from skimage.feature import local_binary_pattern

def extract_hist_lbp(x):
    y = local_binary_pattern(x, P=8, R=1, method='default') # i param. devono essere gli stessi del training set
    h, b = np.histogram(y.flatten(), np.arange(257), density=True)
    return h

h = extract_hist_lbp(x)
h_norm = (h - MU) / (STD + 1e-15)
# non devo calcolare MU e STD sulla nuova immagine, altrimenti non sono più coerente

h_norm = np.reshape(h_norm, (1,256))

# lancio la predizione
predizione = classificatore.predict(h_norm)

# predict vuole una matrice perchè fa la predizione su più immagini contemporaneamente
# in pratica calcola l'equazione Wt x + b = 0 e decide la regione

# calcoliamo le performance di questo classificatore lineare
from glob import glob

list_benign = glob('./Immagini/testset/benign/*.png')
list_feats = list()
list_label = list()

for filename in list_benign:
    x = np.float64(io.imread(filename))
    h = extract_hist_lbp(x)
    list_feats.append(h)
    list_label.append(0) # 0 benigno, 1 maligno
    
    
list_malign = glob('./Immagini/testset/malignant/*.png')
list_feats = list()
list_label = list()

for filename in list_malign:
    x = np.float64(io.imread(filename))
    h = extract_hist_lbp(x)
    list_feats.append(h)
    list_label.append(1) # 0 benigno, 1 maligno    
    

feats_test = np.stack(list_feats, 0)    
label_test = np.stack(list_label)

# prima di fare il predict devo normalizzare
feats_test = (feats_test-MU)/(STD + 1e-15)

predetto = classificatore.predict(feats_test)

# l'accuratezza è calcolata come media del vettore che vale 1 quando
# la predizione è corretta, 0 altrimenti

acc = np.mean(predetto == label_test)

from sklearn import metrics
acc = metrics.accuracy_score(label_test, predetto)
matrix = metrics.confusion_matrix(label_test, predetto)

print(matrix)
print(metrics.classification_report(label_test, predetto))

# numero righe e colonne pari al numero di classi
# colonne: classe predetta
# righe: classe vera