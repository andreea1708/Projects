# -*- coding: utf-8 -*-
"""
Created on Thu May 26 18:01:06 2022

@author: Budeanu Andreea
"""

import sys
import numpy as np
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QWidget,
    QErrorMessage
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from scipy import interpolate


class Window(QMainWindow):
    
    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.n=1
        self.setWindowTitle('B-spline curve')
        self.setWindowIcon(QIcon('logo.ico'))
        self.setStyleSheet("background-color: lightblue")
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setStyleSheet("background-color:white")
        
        self.button = QPushButton('Generate')
        self.button.setStyleSheet("background-color: white; border :1px solid black")
        self.button1 = QPushButton('Clear')
        self.button1.setStyleSheet("background-color: white; border :1px solid black")
        
        self.error_dialog = QErrorMessage()
        self.error_clear = QErrorMessage()

        self.button.clicked.connect(self.bspline)
        self.button1.clicked.connect(self.clear)

        layout = QGridLayout()#QVBoxLayout()
        
        layout.addWidget(self.toolbar,0,0,1,1)
        layout.addWidget(self.canvas,1,0)
        layout.addWidget(self.button,2,0)
        layout.addWidget(self.button1,3,0)

        bx = QLabel('X coordinates:')
        layout.addWidget(bx,0,1)
        self.bxe = QLineEdit()
        self.bxe.setStyleSheet("QLineEdit"
                               "{"
                               "background: white;"
                               "}")
        layout.addWidget(self.bxe,0,2)
        
        
        by = QLabel('Y coordinates:')
        layout.addWidget(by,1,1)
        self.bye = QLineEdit()
        self.bye.setStyleSheet("QLineEdit"
                               "{"
                               "background: white;"
                               "}")
        layout.addWidget(self.bye,1,2)
        
        byexpli = QLabel('Recommendation: Enter the points as in the following example [1,2,3]')
        layout.addWidget(byexpli,2,2)
        byexpli.setStyleSheet("background-color: white; border: 2px solid black")
       
       
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()

        
    def bspline(self):
        self.figure.clear()
        coordonatex=self.bxe.text()
        coordonatey=self.bye.text()
        
        if coordonatex == '' or coordonatey == '':
            self.error_dialog.showMessage('You have no x or y coordinates!')
        
        self.x=np.array([float(i.strip()) for i in coordonatex[1:-1].split(",")])
        self.y=np.array([float(j.strip()) for j in coordonatey[1:-1].split(",")])
        
        if len(self.x)<2 :
            self.error_dialog.showMessage('Enter a number of coordinates greater than 1 at x coordinates!')
        else:
            if len(self.y)<2:
                self.error_dialog.showMessage('Enter a number of coordinates greater than 1 at y coordinates!')
        
        if len(self.x) != len(self.y):
            if len(self.x) > len(self.y):
                self.error_dialog.showMessage('The number of x coordinates is greater than the number of y coordinates!')
            else:
                if len(self.x) < len(self.y):
                    self.error_dialog.showMessage('The number of y coordinates is greater than the number of x coordinates!')
        
        #b-spline
        l=len(self.x)
        t=np.linspace(0,1,l-2,endpoint=True)
        t=np.append([0,0,0],t)
        t=np.append(t,[1,1,1])

        tck=[t,[self.x,self.y],3]
        u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
        out = interpolate.splev(u3,tck)

        plt.plot(self.x,self.y,'k--',label='Control polygon',marker='o',markerfacecolor='red')
        plt.plot(out[0],out[1],'b',linewidth=2.0,label='B-spline curve')
        plt.legend(loc='best')
        plt.axis([min(self.x)-1, max(self.x)+1, min(self.y)-1, max(self.y)+1])
        plt.title('Cubic B-spline curve evaluation')
        self.canvas.draw()

    def clear(self):
        for i in range(len(self.x)):
            np.delete(self.x,i)
        for j in range(len(self.y)):
            np.delete(self.y,j)
        print(self.x)
        print(self.y)
        self.bxe.clear()
        self.bye.clear()
        plt.clf()
        self.figure.clear()
        self.canvas.draw()
        self.n = 0
        self.error_clear.showMessage('No more points! Enter new coordinates!')
        
        
if __name__ == '__main__':
    
    
    
    # creating apyqt5 application
    app = QApplication(sys.argv)
    # creating a window object
    main = Window()
    
    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())
