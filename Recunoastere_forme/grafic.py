import math
from sympy import *
import numpy as np
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDialog,
    QDoubleSpinBox,
    QFontComboBox,
    QGridLayout,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QHBoxLayout,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import pandas as pd

class InterfataStat(QMainWindow):
    def __init__(self,parent=None):

        super(InterfataStat,self).__init__(parent)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.butonRR = QPushButton('RR')
        self.butonAQT = QPushButton('AQT')
        self.butonNN = QRadioButton('Nearest Neighbor')
        self.butonKNN = QRadioButton('K-Nearest Neighbor')
        self.butonEF = QRadioButton('EigenFaces Clasic')
        self.butonEF_clasa = QRadioButton('EigenFaces ReprezentantiClasa')
        self.butonLanczos = QRadioButton('Lanczos')
        self.butonTimpPr = QPushButton('Timp preprocesare')
        self.butonRR.setEnabled(False)
        self.butonAQT.setEnabled(False)
        self.butonTimpPr.setVisible(False)
        alegere_antrenare =['60% Antrenare','80% Antrenare','90% Antrenare']
        self.label_antrenare = QLabel('Antrenare:')

        self.combo_box_antrenare = QComboBox()
        self.combo_box_antrenare.setGeometry(200, 150, 120, 30)
        self.combo_box_antrenare.addItems(alegere_antrenare)

        layout_cbox_antrenare = QVBoxLayout()
        layout_cbox_antrenare.addWidget(self.label_antrenare)
        layout_cbox_antrenare.addWidget(self.combo_box_antrenare)


        layout_alegeri = QVBoxLayout()
        layout_alegeri.addWidget(self.butonNN)
        layout_alegeri.addWidget(self.butonKNN)
        layout_alegeri.addWidget(self.butonEF)
        layout_alegeri.addWidget(self.butonEF_clasa)
        layout_alegeri.addWidget(self.butonLanczos)
        layout = QGridLayout()

        layout.addLayout(layout_alegeri,0,0)
        layout.addLayout(layout_cbox_antrenare,1,0)
        layout.addWidget(self.canvas,2,0)
        layout.addWidget(self.butonRR,3,0)
        layout.addWidget(self.butonAQT,4,0)
        layout.addWidget(self.butonTimpPr,5,0)

        
        self.butonAQT.clicked.connect(self.arata_AQT)
        self.butonRR.clicked.connect(self.arata_RR)
        self.butonTimpPr.clicked.connect(self.arata_timp_preproc)
        self.butonNN.clicked.connect(self.alegere_algoritm)
        self.butonKNN.clicked.connect(self.alegere_algoritm)
        self.butonEF.clicked.connect(self.alegere_algoritm)
        self.butonEF_clasa.clicked.connect(self.alegere_algoritm)
        self.butonLanczos.clicked.connect(self.alegere_algoritm)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        #self.show()

    def arata_AQT(self):
        
        if self.alegere_algoritm() == 1:
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiNN_KNN60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiNN_KNN80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiNN_KNN90%.csv')

            self.figure.clear()
            ax = self.figure.add_subplot(171)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'K-Nearest Neighbor') & (
            self.fis['K'] == '3')]
            ax.set_title('kNN-3')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])
            
            ax = self.figure.add_subplot(173)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'K-Nearest Neighbor') & (
            self.fis['K'] == '5')]
            ax.set_title('kNN-5')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])
            
            ax = self.figure.add_subplot(175)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'K-Nearest Neighbor') & (
            self.fis['K'] == '7')]
            ax.set_title('kNN-7')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(177)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'K-Nearest Neighbor') & (
            self.fis['K'] == '9')]
            ax.set_title('kNN-9')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            self.canvas.draw()
            self.show()

        elif self.alegere_algoritm() == 0:
           
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiNN_KNN60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiNN_KNN80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiNN_KNN90%.csv')
            self.figure.clear()
            ax = self.figure.add_subplot(151)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Nearest Neighbor')]
            ax.set_title('NN')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            self.canvas.draw()
            self.show()
        
        elif self.alegere_algoritm() == 3:
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasic60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasic80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiEFClasic90%.csv')
            self.figure.clear()
            ax = self.figure.add_subplot(191)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 20)]
            ax.set_title('EFClasic K-20')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(193)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 40)]
            ax.set_title('EFClasic K-40')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(195)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 60)]
            ax.set_title('EFClasic K-60')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(197)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 80)]
            ax.set_title('EFClasic K-80')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(199)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 100)]
            ax.set_title('EFClasic K-100')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            self.canvas.draw()
            self.show()
        
        elif self.alegere_algoritm() == 4:
            self.figure.clear()
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasa60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasa80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiEFClasa90%.csv')
            self.figure.clear()
            ax = self.figure.add_subplot(191)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 20)]
            ax.set_title('EFClasa K-20')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(193)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 40)]
            ax.set_title('EFClasa K-40')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(195)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 60)]
            ax.set_title('EFClasa K-60')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(197)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 80)]
            ax.set_title('EFClasa K-80')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(199)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 100)]
            ax.set_title('EFClasa K-100')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])
            self.canvas.draw()
            self.show()
        
        elif self.alegere_algoritm() == 5:
            self.figure.clear()
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiLanczos60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiLanczos80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiLanczos90%.csv')
            self.figure.clear()
            ax = self.figure.add_subplot(191)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 20)]
            ax.set_title('Laz K-20')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(193)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 40)]
            ax.set_title('Laz K-40')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(195)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 60)]
            ax.set_title('Laz K-60')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(197)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 80)]
            ax.set_title('Laz K-80')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])

            ax = self.figure.add_subplot(199)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 100)]
            ax.set_title('Laz K-100')
            ax.set_xlabel('Norma')
            ax.set_ylabel('AQT')
            ax.plot(stat['Norma'], stat['AQT'])
            self.canvas.draw()
            self.show()

        


    def arata_RR(self):
        
        if self.alegere_algoritm() == 1:
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiNN_KNN60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiNN_KNN80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiNN_KNN90%.csv')

            
            self.figure.clear()
            ax = self.figure.add_subplot(171)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'K-Nearest Neighbor') & (
            self.fis['K'] == '3')]
            ax.set_title('kNN-3')
            ax.set_xlabel('Norma')
            ax.set_ylabel('RR')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(173)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'K-Nearest Neighbor') & (
            self.fis['K'] == '5')]
            ax.set_title('kNN-5')
            ax.set_xlabel('Norma')
            ax.set_ylabel('RR')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(175)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'K-Nearest Neighbor') & (
            self.fis['K'] == '7')]
            ax.set_title('kNN-7')
            ax.set_xlabel('Norma')
            ax.set_ylabel('RR')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(177)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'K-Nearest Neighbor') & (
            self.fis['K'] == '9')]
            ax.set_title('kNN-9')
            ax.set_xlabel('Norma')
            ax.set_ylabel('RR')
            ax.plot(stat['Norma'], stat['Rata'])

            self.canvas.draw()
            self.show()
        
        elif self.alegere_algoritm() == 0:
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiNN_KNN60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiNN_KNN80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiNN_KNN90%.csv')
            self.figure.clear()
            ax = self.figure.add_subplot(151)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Nearest Neighbor')]
            ax.set_title('NN')
            ax.set_xlabel('Norma')
            ax.set_ylabel('RR')
            ax.plot(stat['Norma'], stat['Rata'])

            self.canvas.draw()
            self.show()
        
        elif self.alegere_algoritm() == 3:
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasic60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasic80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiEFClasic90%.csv')
            self.figure.clear()
            ax = self.figure.add_subplot(191)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 20)]
            ax.set_title('EFClasic K-20')
            ax.set_xlabel('Norma')
            ax.set_ylabel('RR')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(193)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 40)]
            ax.set_title('EFClasic K-40')
            ax.set_xlabel('Norma')
            ax.set_ylabel('RR')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(195)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 60)]
            ax.set_title('EFClasic K-60')
            ax.set_xlabel('Norma')
            ax.set_ylabel('RR')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(197)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 80)]
            ax.set_title('EFClasic K-80')
            ax.set_xlabel('Norma')
            ax.set_ylabel('RR')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(199)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 100)]
            ax.set_title('EFClasic K-100')
            ax.set_xlabel('Norma')
            ax.set_ylabel('RR')
            ax.plot(stat['Norma'], stat['Rata'])

            self.canvas.draw()
            self.show()

        
        elif self.alegere_algoritm() == 4:
            self.figure.clear()
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasa60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasa80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiEFClasa90%.csv')
            self.figure.clear()
            ax = self.figure.add_subplot(191)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 20)]
            ax.set_title('EFClasa K-20')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Rata')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(193)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 40)]
            ax.set_title('EFClasa K-40')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Rata')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(195)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 60)]
            ax.set_title('EFClasa K-60')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Rata')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(197)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 80)]
            ax.set_title('EFClasa K-80')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Rata')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(199)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 100)]
            ax.set_title('EFClasa K-100')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Rata')
            ax.plot(stat['Norma'], stat['Rata'])

            self.canvas.draw()
            self.show()
        
        elif self.alegere_algoritm() == 5:
            self.figure.clear()
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiLanczos60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiLanczos80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiLanczos90%.csv')
            self.figure.clear()
            ax = self.figure.add_subplot(191)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 20)]
            ax.set_title('Laz K-20')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Rata')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(193)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 40)]
            ax.set_title('Laz K-40')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Rata')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(195)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 60)]
            ax.set_title('Laz K-60')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Rata')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(197)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 80)]
            ax.set_title('Laz K-80')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Rata')
            ax.plot(stat['Norma'], stat['Rata'])

            ax = self.figure.add_subplot(199)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 100)]
            ax.set_title('Laz K-100')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Rata')
            ax.plot(stat['Norma'], stat['Rata'])
            self.canvas.draw()
            self.show()

        
    def arata_timp_preproc(self):
        if self.alegere_algoritm() == 3:
            self.figure.clear()
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasic60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasic80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiEFClasic90%.csv')
            self.figure.clear()
            ax = self.figure.add_subplot(191)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 20)]
            ax.set_title('EFClasic K-20')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(193)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 40)]
            ax.set_title('EFClasic K-40')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(195)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 60)]
            ax.set_title('EFClasic K-60')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(197)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 80)]
            ax.set_title('EFClasic K-80')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(199)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasic') & (
            self.fis['K'] == 100)]
            ax.set_title('EFClasic K-100')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            self.canvas.draw()
            self.show()

        elif self.alegere_algoritm() == 4:
            self.figure.clear()
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasa60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiEFClasa80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiEFClasa90%.csv')
            self.figure.clear()
            ax = self.figure.add_subplot(191)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 20)]
            ax.set_title('EFClasa K-20')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(193)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 40)]
            ax.set_title('EFClasa K-40')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(195)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 60)]
            ax.set_title('EFClasa K-60')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(197)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 80)]
            ax.set_title('EFClasa K-80')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(199)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'EigenFaces Clasa') & (
            self.fis['K'] == 100)]
            ax.set_title('EFClasa K-100')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            self.canvas.draw()
            self.show()

        elif self.alegere_algoritm() == 5:
            self.figure.clear()
            if (self.combo_box_antrenare.currentText() == '60% Antrenare'):
                self.fis = pd.read_csv('StatisticiLanczos60%.csv')

            elif (self.combo_box_antrenare.currentText() == '80% Antrenare'):
                self.fis = pd.read_csv('StatisticiLanczos80%.csv')

            else:
                self.fis = pd.read_csv('StatisticiLanczos90%.csv')
            self.figure.clear()
            ax = self.figure.add_subplot(191)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 20)]
            ax.set_title('Laz K-20')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp Preprocesare')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(193)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 40)]
            ax.set_title('Laz K-40')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp Preprocesare')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(195)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 60)]
            ax.set_title('Laz K-60')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp Preprocesare')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(197)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 80)]
            ax.set_title('Laz K-80')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp Preprocesare')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])

            ax = self.figure.add_subplot(199)
            stat = self.fis.loc[(self.fis['Algoritm'] == 'Lanczos') & (
            self.fis['K'] == 100)]
            ax.set_title('Laz K-100')
            ax.set_xlabel('Norma')
            ax.set_ylabel('Timp Preprocesare')
            ax.plot(stat['Norma'], stat['Timp Preprocesare'])
            self.canvas.draw()
            self.show()



    def alegere_algoritm(self):
        contor = 0
        if self.butonNN.isChecked():
            self.butonTimpPr.setVisible(False)
            self.butonRR.setEnabled(True)
            self.butonAQT.setEnabled(True)
            self.butonRR.setText('RR pentru Nearest Neighbor')
            self.butonAQT.setText('AQT pentru Nearest Neighbor')

        elif self.butonKNN.isChecked():
            self.butonTimpPr.setVisible(False)
            self.butonRR.setEnabled(True)
            self.butonAQT.setEnabled(True)
            self.butonRR.setText('RR pentru K-Nearest Neighbor')
            self.butonAQT.setText('AQT pentru K-Nearest Neighbor')
            contor = 1
        
        elif self.butonEF.isChecked():
            self.butonTimpPr.setVisible(True)
            self.butonRR.setEnabled(True)
            self.butonAQT.setEnabled(True)
            self.butonRR.setText('RR pentru EigenFaces Clasic')
            self.butonAQT.setText('AQT pentru EigenFaces Clasic')
            self.butonTimpPr.setText('Timp Preprocesare pentru EigenFaces Clasic')
            contor = 3
        

        elif self.butonEF_clasa.isChecked():
            self.butonTimpPr.setVisible(True)
            self.butonRR.setEnabled(True)
            self.butonAQT.setEnabled(True)
            self.butonRR.setText('RR pentru EigenFaces Clasa')
            self.butonAQT.setText('AQT pentru EigenFaces Clasa')
            self.butonTimpPr.setText('Timp Preprocesare pentru EigenFaces Clasa')
            contor = 4

        else:
            self.butonTimpPr.setVisible(True)
            self.butonRR.setEnabled(True)
            self.butonAQT.setEnabled(True)
            self.butonRR.setText('RR pentru Lanczos')
            self.butonAQT.setText('AQT pentru Lanczos')
            self.butonTimpPr.setText('Timp Preprocesare pentru Lanczos')
            contor = 5

        return contor

      

if __name__ == '__main__':
    
    
    
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = InterfataStat()
    
    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())