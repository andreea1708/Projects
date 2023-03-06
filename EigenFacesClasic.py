# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:27:18 2022

@author: Laptop
"""
from scipy.sparse import linalg
import cv2, numpy as np
from matplotlib import pyplot as plt
from numpy import linalg as la

caleBD = r'D:\\Ore_facultate\\An_3\\ACS\\ACS\\baze\\'

nrPozeAntrenare = 8
nrPers = 40
nrPixeli = 10304
nrPozePersoane = 10
K=20

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

def preprocesareEigenFacesClasic(A, K):
    media = np.mean(A,axis = 1) 
    A=(A.T-media).T 
    cov = A@A.T 
    d, v = linalg.eigs(cov,K)
    indici = np.argsort(d) 
    indici = indici[-1:-K-1:-1] 
    HQPB = v[:,indici] 
    proiectii = A.T @ HQPB 
    return [media,proiectii,HQPB]
     
def preprocesareEigenFacesOptimizat(A, K):
    media = np.mean(A,axis = 1) 
    A=(A.T-media).T 
    cov = A@A.T 
    d, v = linalg.eig(cov)
    v = A@v
    indici = np.argsort(d) 
    indici = indici[-1:-K-1:-1] 
    HQPB = v[:,indici] 
    proiectii = A.T @ HQPB 
    return [media,proiectii,HQPB]

A = configurareA(caleBD)
media, proiectii, HQPB=preprocesareEigenFacesClasic(A, K)
poza_test = r'D:\\Ore_facultate\\An_3\\ACS\\ACS\\baze\\s4\\9.pgm'
poza_test = cv2.imread(poza_test, 0)
poza_test = np.array(poza_test)
plt.imshow(poza_test, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()
poza_test = np.reshape(poza_test, (-1, ))
poza_test=poza_test - media #centrare in jururl mediei
pr_test=poza_test @ HQPB


poza_test = np.reshape(poza_test, (-1, ))
norma = 1
pozitia_gasita = NN(proiectii.T, pr_test, norma)

pozaGasita = np.reshape(A[:, pozitia_gasita], (112, 92))
plt.imshow(pozaGasita, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()