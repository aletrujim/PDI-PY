import numpy as np
import matplotlib.pyplot as plt

import sys
import cv2
from novogui3 import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Main(QMainWindow):        
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
                        
        self.ui.Carregar.clicked.connect(self.colormaps)
        self.ui.comboBox.activated.connect(self.plot)
        
        #initial show
        img = cv2.imread("plot.png")           
        height, width, channels = img.shape
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)           
        img=QtGui.QImage(img, width, height, QtGui.QImage.Format_RGB888)
        img=QtGui.QPixmap.fromImage(img)                
        self.ui.ImagemOri.setPixmap(img) 
                
        global cmaps
        cmaps = ['binary', 'Reds', 'Greens', 'Blues','Greys', 'Oranges', 'Purples',                              
         'gist_earth', 'gist_ncar', 'gist_rainbow', 'gist_stern', 'jet', 'brg', 'CMRmap', 
         'cubehelix','gnuplot', 'gnuplot2', 'ocean', 'rainbow','terrain', 'flag', 'prism']
        
        global nr, gra
        nr = len(cmaps)
        gra = np.linspace(0, 1, 256)
        gra = np.vstack((gra, gra))
        
        self.ui.comboBox.addItems(cmaps)
               
    def colormaps(self):       
        fig, axes = plt.subplots(nr-1)
        fig.subplots_adjust(top=0.9, bottom=0.01, left=0.2, right=0.9)
        axes[0].set_title('algunos colormaps de cmap', fontsize=10)
        
        for ax, cm in zip(axes, cmaps):
            ax.imshow(gra, aspect='auto', cmap=plt.get_cmap(cm))
            pos = list(ax.get_position().bounds)
            x = pos[0] - 0.01
            y = pos[1] + pos[3]/2.
            fig.text(x, y, cm, va='center', ha='right', fontsize=10)
            ax.set_axis_off()       
            
        plt.show()
                        
    def plot(self):
        pal = str(self.ui.comboBox.currentText())
        
        def f(x, y): 
            return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 -y ** 2) 
        
        n = 256 
        x = np.linspace(-3, 3, n) 
        y = np.linspace(-3, 3, n) 
        X, Y = np.meshgrid(x, y) 
        plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.get_cmap(pal)) 
        
        plt.axis([-3, 3, -3, 3])
        plt.savefig("newplot.png")
               
        img = cv2.imread("newplot.png")           
        height, width, channels = img.shape
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)           
        img=QtGui.QImage(img, width, height, QtGui.QImage.Format_RGB888)
        img=QtGui.QPixmap.fromImage(img)                
        self.ui.ImagemOri.setPixmap(img)         
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
        

