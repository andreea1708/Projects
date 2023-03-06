# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:19:54 2022

@author: Eduard
"""
import cv2, numpy as np
from matplotlib import pyplot as plt
from numpy import linalg as la

caleBD = r'D:\\Ore_facultate\\An_3\\ACS\\ACS\\baze\\'

nrPozeAntrenare = 8
nrPers = 40
nrPixeli = 10304
nrPozePersoane = 10

def configurareA(caleBD):
    A = np.zeros((nrPixeli, nrPozeAntrenare * nrPers))
    for i in range(1, nrPers + 1):
        caleFolderPers = caleBD + 's' + str(i) + '\\'
        for j in range(1, nrPozeAntrenare + 1):
            calePoza = caleFolderPers + str(j) + '.pgm'
            poza = cv2.imread(calePoza, 0)
            poza = np.array(poza)
            plt.imshow(poza, cmap = 'gray', vmin = 0, vmax = 255)
            #plt.show()
            poza = np.reshape(poza,(nrPixeli, ))
            A[:, (i - 1) * nrPozeAntrenare + j - 1] = poza
    return A

def NN(A, poza_test,norma):
    z = np.zeros(len(A[0]))
    for i in range(len(A[0])):
        z[i] = la.norm(A[:, i] - poza_test, norma)
    pozitia = np.argmin(z)
    return pozitia
 

A = configurareA(caleBD)
poza_test = r'D:\\Ore_facultate\\An_3\\ACS\\ACS\\baze\\s2\\9.pgm'
poza_test = cv2.imread(poza_test, 0)
poza_test = np.array(poza_test)
plt.imshow(poza_test, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()

poza_test = np.reshape(poza_test, (-1, ))
norma = 1
pozitia = NN(A, poza_test, norma)

pozaGasita = np.reshape(A[:, pozitia], (112, 92))
plt.imshow(pozaGasita, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()