import sys
import cv2
import numpy as np
from scipy.sparse import linalg
from PyQt5.QtCore import *
from PyQt5.QtGui import *
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
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox
    
    
)
import win32api

class InterfataPrincipala(QMainWindow):

    def __init__(self,parent=None):
        
        
        super(InterfataPrincipala,self).__init__(parent)
        self.setWindowTitle("M4")
        self.btn_poza = QPushButton('Selecteaza poza')
        self.btn_poza.clicked.connect(self.getPoza)
        self.label_rezultat = QLabel(self)
        self.label_tine_minte_cale = QLabel('')
        self.poza_aleasa = QLabel()

        self.efect_flip = QPushButton('Flip')
        self.efect_dilatare = QPushButton('Dilatare')
        self.efect_erodare = QPushButton('Erodare')
        self.efect_blurgaussian = QPushButton('Blur Gaussian')
        self.efect_filtrubilateral = QPushButton('Filtru bilateral')
        self.efect_medianblur = QPushButton('Median blur')
        self.efect_text = QPushButton('Adaugare text')
        self.efect_resize = QPushButton('Redimensionare')
        self.efect_rotire = QPushButton('Rotire imagine')
        self.translatare = QPushButton('Translatare imagine')
        self.canalcolor = QPushButton('Schimbare color')

        self.efect_flip.clicked.connect(self.flip_poza)
        self.efect_dilatare.clicked.connect(self.dilatare_poza)
        self.efect_erodare.clicked.connect(self.erodare_poza)
        self.efect_filtrubilateral.clicked.connect(self.filtru_bilateral)
        self.efect_blurgaussian.clicked.connect(self.blur_gaussian)
        self.efect_text.clicked.connect(self.pune_text)
        self.efect_medianblur.clicked.connect(self.median_blur)
        self.efect_resize.clicked.connect(self.redimensionare_img)
        self.efect_rotire.clicked.connect(self.rotire_img)
        self.translatare.clicked.connect(self.translateaza_img)
        self.canalcolor.clicked.connect(self.canale_color_img)

        layout_poze = QHBoxLayout()
        layout_poze.addWidget(self.poza_aleasa)
        layout_poze.addWidget(self.label_rezultat)



        layout_principal = QGridLayout()
        layout_principal.addLayout(layout_poze,0,0)
        layout_principal.addWidget(self.btn_poza,1,0)
        layout_principal.addWidget(self.efect_flip,2,0)
        layout_principal.addWidget(self.efect_dilatare,3,0)
        layout_principal.addWidget(self.efect_erodare,4,0)
        layout_principal.addWidget(self.efect_blurgaussian,5,0)
        layout_principal.addWidget(self.efect_filtrubilateral,6,0)
        layout_principal.addWidget(self.efect_medianblur,7,0)
        layout_principal.addWidget(self.efect_text,8,0)
        layout_principal.addWidget(self.efect_resize,9,0)
        layout_principal.addWidget(self.efect_rotire,10,0)
        layout_principal.addWidget(self.translatare,11,0)
        layout_principal.addWidget(self.canalcolor,12,0)

        widget = QWidget()
        widget.setLayout(layout_principal)
        self.setCentralWidget(widget)
        self.show()

    def getPoza(self):
        self.label_rezultat.clear()
        
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'D:\Ore_facultate\An_3\ACS\ACS\lab\M4',"Image files (*.jpg *.gif)")
        self.poza_aleasa.setPixmap(QPixmap(fname[0]))
        self.label_tine_minte_cale.setText(fname[0])

    
    def flip_poza(self):
        self.label_rezultat.clear()
        cale = self.label_tine_minte_cale.text()
        
        if(len(cale) == 0):
            win32api.MessageBox('0','Te rog alege poza!','Eroare')
            return
        pozaTest = cv2.imread(cale)
        pozaTest=cv2.cvtColor(pozaTest, cv2.COLOR_BGR2RGB)
        self.rez = cv2.flip(pozaTest,1)
        self.convert = QImage(self.rez, self.rez.shape[1], self.rez.shape[0], self.rez.strides[0], QImage.Format_RGB888)
        self.label_rezultat.setPixmap(QPixmap.fromImage(self.convert))
    
    def dilatare_poza(self):
        self.label_rezultat.clear()
        cale = self.label_tine_minte_cale.text()
        
        if(len(cale) == 0):
            win32api.MessageBox('0','Te rog alege poza!','Eroare')
            return
        pozaTest = cv2.imread(cale)
        pozaTest=cv2.cvtColor(pozaTest, cv2.COLOR_BGR2RGB)
        kernel = np.ones((5, 5), np.uint8)
        self.rez = cv2.dilate(pozaTest, kernel, iterations=1)
        self.convert = QImage(self.rez, self.rez.shape[1], self.rez.shape[0], self.rez.strides[0], QImage.Format_RGB888)
        self.label_rezultat.setPixmap(QPixmap.fromImage(self.convert))

    def erodare_poza(self):
        self.label_rezultat.clear()
        cale = self.label_tine_minte_cale.text()
        
        if(len(cale) == 0):
            win32api.MessageBox('0','Te rog alege poza!','Eroare')
            return
        pozaTest = cv2.imread(cale)
        pozaTest=cv2.cvtColor(pozaTest, cv2.COLOR_BGR2RGB)
        kernel = np.ones((5, 5), np.uint8)
        self.rez = cv2.erode(pozaTest, kernel, iterations=1)
        self.convert = QImage(self.rez, self.rez.shape[1], self.rez.shape[0], self.rez.strides[0], QImage.Format_RGB888)
        self.label_rezultat.setPixmap(QPixmap.fromImage(self.convert))

    def filtru_bilateral(self):
        self.label_rezultat.clear()
        cale = self.label_tine_minte_cale.text()
        
        if(len(cale) == 0):
            win32api.MessageBox('0','Te rog alege poza!','Eroare')
            return
        pozaTest = cv2.imread(cale)
        pozaTest=cv2.cvtColor(pozaTest, cv2.COLOR_BGR2RGB)
        self.rez = cv2.bilateralFilter(pozaTest,d=15,sigmaColor=75,sigmaSpace=75)
        self.convert = QImage(self.rez, self.rez.shape[1], self.rez.shape[0], self.rez.strides[0], QImage.Format_RGB888)
        self.label_rezultat.setPixmap(QPixmap.fromImage(self.convert))
    
    def blur_gaussian(self):
        self.label_rezultat.clear()
        cale = self.label_tine_minte_cale.text()
        
        if(len(cale) == 0):
            win32api.MessageBox('0','Te rog alege poza!','Eroare')
            return
        pozaTest = cv2.imread(cale)
        pozaTest=cv2.cvtColor(pozaTest, cv2.COLOR_BGR2RGB)
        borderSize = (5,5)
        self.rez = cv2.GaussianBlur(pozaTest,borderSize,cv2.BORDER_DEFAULT)
        self.convert = QImage(self.rez, self.rez.shape[1], self.rez.shape[0], self.rez.strides[0], QImage.Format_RGB888)
        self.label_rezultat.setPixmap(QPixmap.fromImage(self.convert))

    def pune_text(self):
        self.label_rezultat.clear()
        cale = self.label_tine_minte_cale.text()
        
        if(len(cale) == 0):
            win32api.MessageBox('0','Te rog alege poza!','Eroare')
            return
        pozaTest = cv2.imread(cale)
        pozaTest=cv2.cvtColor(pozaTest, cv2.COLOR_BGR2RGB)
        org = (50,50)
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (0, 255, 0)
        fontScale = 1
        thickness = 2
        self.rez = cv2.putText(pozaTest, 'Poza', org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
        self.convert = QImage(self.rez, self.rez.shape[1], self.rez.shape[0], self.rez.strides[0], QImage.Format_RGB888)
        self.label_rezultat.setPixmap(QPixmap.fromImage(self.convert))
    
    def median_blur(self):
        self.label_rezultat.clear()
        cale = self.label_tine_minte_cale.text()
        
        if(len(cale) == 0):
            win32api.MessageBox('0','Te rog alege poza!','Eroare')
            return
        pozaTest = cv2.imread(cale)
        pozaTest=cv2.cvtColor(pozaTest, cv2.COLOR_BGR2RGB)
        self.rez = cv2.medianBlur(pozaTest,5)
        self.convert = QImage(self.rez, self.rez.shape[1], self.rez.shape[0], self.rez.strides[0], QImage.Format_RGB888)
        self.label_rezultat.setPixmap(QPixmap.fromImage(self.convert))
    
    def redimensionare_img(self):
        self.label_rezultat.clear()
        cale = self.label_tine_minte_cale.text()
        
        if(len(cale) == 0):
            win32api.MessageBox('0','Te rog alege poza!','Eroare')
            return
        pozaTest = cv2.imread(cale)
        pozaTest=cv2.cvtColor(pozaTest, cv2.COLOR_BGR2RGB)
        self.rez = cv2.resize(pozaTest, (125, 225),
               interpolation = cv2.INTER_LINEAR)
        self.convert = QImage(self.rez, self.rez.shape[1], self.rez.shape[0], self.rez.strides[0], QImage.Format_RGB888)
        self.label_rezultat.setPixmap(QPixmap.fromImage(self.convert))
    
    def rotire_img(self):
        self.label_rezultat.clear()
        cale = self.label_tine_minte_cale.text()
        
        if(len(cale) == 0):
            win32api.MessageBox('0','Te rog alege poza!','Eroare')
            return
        pozaTest = cv2.imread(cale)
        pozaTest=cv2.cvtColor(pozaTest, cv2.COLOR_BGR2RGB)
        self.rez = cv2.rotate(pozaTest,cv2.ROTATE_180)
        self.convert = QImage(self.rez, self.rez.shape[1], self.rez.shape[0], self.rez.strides[0], QImage.Format_RGB888)
        self.label_rezultat.setPixmap(QPixmap.fromImage(self.convert))

    def translateaza_img(self):
        self.label_rezultat.clear()
        cale = self.label_tine_minte_cale.text()
        
        if(len(cale) == 0):
            win32api.MessageBox('0','Te rog alege poza!','Eroare')
            return
        pozaTest = cv2.imread(cale)
        pozaTest=cv2.cvtColor(pozaTest, cv2.COLOR_BGR2RGB)
        inaltime,latime = pozaTest.shape[:2]
        dim_i,dim_l = inaltime / 4, latime / 4
        matrice_translatie = np.float32([[1,0,dim_i],[0,1,dim_l]])
        self.rez = cv2.warpAffine(pozaTest,matrice_translatie,(inaltime,latime))
        self.convert = QImage(self.rez, self.rez.shape[1], self.rez.shape[0], self.rez.strides[0], QImage.Format_RGB888)
        self.label_rezultat.setPixmap(QPixmap.fromImage(self.convert))

    def canale_color_img(self):
        self.label_rezultat.clear()
        cale = self.label_tine_minte_cale.text()
        
        if(len(cale) == 0):
            win32api.MessageBox('0','Te rog alege poza!','Eroare')
            return
        pozaTest = cv2.imread(cale)
        #self.rez = cv2.cvtColor(pozaTest,cv2.COLOR_BGR2RGB)
        self.convert = QImage(pozaTest, pozaTest.shape[1], pozaTest.shape[0], pozaTest.strides[0], QImage.Format_RGB888)
        self.label_rezultat.setPixmap(QPixmap.fromImage(self.convert))
    

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    main = InterfataPrincipala()
    
    main.show()
    
    sys.exit(app.exec_())  

