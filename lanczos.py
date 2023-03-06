import cv2
import numpy as np
#from matplotlib import pyplot as plt
#import statistics
#import time
#from scipy.sparse import linalg
#import math
import pandas as pd

caleBD = "D:\\Ore_facultate\\An_3\\ACS\\ACS\\baze\\"

poza = caleBD + "s"

nrPers = 40
nrPozeAntrenate = 8
nrPixeli = 112*92
nr_total_teste = 80

stat = pd.read_csv("stat.txt", sep=" ", names=["Algoritm", "Norma", "K", "Rata", "AQT", "Timp Preprocesare"])

def configurareA(caleBD):
    A = np.zeros((nrPixeli,nrPozeAntrenate * nrPers))

    for i in range(1,nrPers+1):
        caleFolder = caleBD + '\s' + str(i) + '\\'
        for j in range(1,nrPozeAntrenate + 1):
            calePoza = caleFolder + str(j) + '.pgm'
            poza = cv2.imread(calePoza,0)
            poza = np.array(poza)
#poza j a persoane i va fi pe coloana (i-1) * nrPoze + (j-1)            
            pozaVect = np.reshape(poza,(10304,))
            A[:,(i - 1) * nrPozeAntrenate+ (j - 1)] = pozaVect
    return A

def NN(A,pozaTest,norma):
        z = np.zeros(len(A[0]))
        #pozaTest = pozaTest.reshape(1,-1)
        for i in range (A.shape[1]):
            if(norma == 'cos'):
                z[i] = 1-(np.dot(A[:,i],pozaTest) / (np.linalg.norm(A[:,i]) * np.linalg.norm(pozaTest)))
            else:
                z[i] = np.linalg.norm(A[:,i] - pozaTest,norma)
        pozitia = np.argmin(z)
        
        return pozitia

    
def Lanczos(A,k):
    m = 10304
    q = np.zeros((m,k+2))
    q[:,0] = np.zeros(m)
    q[:,1] = np.ones(m)
    q[:,1] = q[:,1] / np.linalg.norm(q[:,1])
    B = 0
    q[0] = 0
    for i in range (1,k + 1):
        w = A @ (A.T@q[:,i]) - B * q[:,i-1]
        l = np.dot(w,q[:,i])
        w = w - l*q[:,i]
        B = np.linalg.norm(w, )
        q[:,i+1]=w / B
    HQPB=q[:,2:] 
    proiectii = A.T @ HQPB
    return proiectii, HQPB

A = configurareA("D:\\Ore_facultate\\An_3\\ACS\\ACS\\baze\\")

proiectii,HQPB = Lanczos(A,20)

pozaTest = "D:\\Ore_facultate\\An_3\\ACS\\ACS\\baze\\s4\\9.pgm"
pozaTest = cv2.imread(pozaTest,0)
cv2.imshow('Aleasa',pozaTest)
pozaTest = np.array(pozaTest)
cv2.imshow('Aleasa',pozaTest)
pozaTest = pozaTest.reshape((-1,))
pr_test = pozaTest @ HQPB
norma = 1
index = NN(proiectii.T,pr_test,norma)
img=index%8+1
index//=8
index+=1

poza_prezisa = cv2.imread(caleBD + f'\s{index}\{img}.pgm')
cv2.imshow('Prezisa',poza_prezisa)
cv2.waitKey(0)


