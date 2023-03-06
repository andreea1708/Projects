import cv2, numpy as np
import statistics
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
 
def kNN(A, K, poza_test,norma):
    z = np.zeros(len(A[0]))
    for i in range(len(A[0])):
        if (norma == 'cos'):
            z[i] = 1 - np.dot(A[:, i], poza_test)/(la.norm(A[:, i]) * la.norm(poza_test))
        else:
            z[i] = la.norm(A[:, i] - poza_test, norma)
    pozitii = np.argsort(z)
    pozitii = pozitii[:K]
    persoane = pozitii //8 + 1
    persoana = statistics.mode(persoane)
    return (persoana - 1) * 8

A = configurareA(caleBD)
poza_test = r'D:\\Ore_facultate\\An_3\\ACS\\ACS\\baze\\s2\\1.pgm'
poza_test = cv2.imread(poza_test, 0)
poza_test = np.array(poza_test)
plt.imshow(poza_test, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()

poza_test = np.reshape(poza_test, (-1, ))
norma = 1
k = 3
pozitiaKNN = kNN(A, k, poza_test, norma)
print(pozitiaKNN)
pozaGasita = np.reshape(A[:, pozitiaKNN], (112, 92))
plt.imshow(pozaGasita, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()
