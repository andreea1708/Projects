import cv2
import numpy as np
from matplotlib import pyplot as plt
import statistics
import time
from scipy.sparse import linalg
import math
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


def K_NN(A,pozaTest,norma,k):
    
    z = np.zeros(len(A[0]))
    pozaTest = pozaTest.reshape(1,-1)
    for i in range (A.shape[1]):
        if(norma == 'cos'):
            z[i] = 1-(np.dot(A[:,i],pozaTest) / (np.linalg.norm(A[:,i]) * np.linalg.norm(pozaTest)))
        else:
            z[i] = np.linalg.norm(A[:,i] - pozaTest,norma)
    pozitii = np.argsort(z)
    pozitii = pozitii[:k]
    persoane = pozitii//8 + 1
    persoana = statistics.mode(persoane)
    return (persoana - 1) * 8

    # creem o noua matrice in care stocam doar o poza RC[:,i] = np.mean(A[:,(i-1)*8]:(i*8-1))
    # Alternativ: RC[:,i] = A[:,np.random.randint((i-1)*8,i*8)]
    # RC = np.zeros(len(A),40)

def preprocesare_EFClasa(A,k):
    RC = np.zeros((10304,40))
    for i in range(40):
        RC[:,i] = np.mean(A[:,((i - 1) * 8):((i * 8) - 1)],axis=1)
    media = np.mean(RC,axis = 1)   

    RC = (RC.T - media).T
    cov = RC@RC.T
    d, v = linalg.eigs(cov,k,which='LM')
    indici = np.argsort(d)
    indici = indici[-1:-k-1:-1]
    HQPB = v[:,indici]
    proiectii = RC.T @ HQPB
    return [media,proiectii,HQPB]

    
"""def statistici(k,norma):
        A = configurareA("D:\\Ore_facultate\\An_3\\ACS\\ACS\\baze\\")
        media,proiectii,HQPB = preprocesare_EFClasa(A,k)
        recunoasteri_corecte = 0
        timp = 0
        timp_initial = time.perf_counter()
        for i in range(1, nrPers+1):
            for j in range(9, 11):
                poza_test = cv2.imread(caleBD + f'/s{i}/{j}.pgm', 0)
                poza_test = np.array(poza_test).reshape((-1,))
                timp_start = time.perf_counter()
                poza_test = poza_test - media
                pr_test = poza_test @ HQPB
                index = NN(proiectii.T,pr_test,norma)
               
                timp_stop = time.perf_counter()
                timp_preproc = timp_stop-timp_initial
                timp = timp + timp_stop-timp_start
                if index == i:
                    recunoasteri_corecte += 1
        
        #print(f'Rata de recunoastere: {recunoasteri_corecte / nr_total_teste * 100}%\n' , f'AQT: {(timp / 80)} secunde')  
        return recunoasteri_corecte / nr_total_teste * 100, timp / 80, timp_preproc * 100


def importare_date():
        norme = [1,2,math.inf,'cos']
        k = [20,40,60,80,100]

        for norma_index in norme:
            for k_index in k:
                rata,aqt,preproc = statistici(k_index,norma_index)
                stat.loc[len(stat.index)] =['EigenFaces Clasic',norma_index,k_index,rata,aqt,preproc]
        
        stat.to_csv('StatisticiEigenFaces.csv', index=False)

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
"""
A = configurareA("D:\\Ore_facultate\\An_3\\ACS\\ACS\\baze\\")

media,proiectii,HQPB = preprocesare_EFClasa(A,20)

pozaTest = "D:\\Ore_facultate\\An_3\\ACS\\ACS\\baze\\s4\\9.pgm"
pozaTest = cv2.imread(pozaTest,0)
cv2.imshow('Aleasa',pozaTest)
pozaTest = np.array(pozaTest)
cv2.imshow('Aleasa',pozaTest)
pozaTest = pozaTest.reshape((-1,))
pozaTest = pozaTest - media
pr_test = pozaTest @ HQPB
norma = 1
index = NN(proiectii.T,pr_test,norma)
#print(index)
if index == 0:
    index += 1
img = 1

poza_prezisa = cv2.imread(caleBD + f'\s{index}\{img}.pgm')
cv2.imshow('Prezisa',poza_prezisa)
cv2.waitKey(0)


