import sys
import cv2 #opencv

from gui2 import Ui_MainWindow

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog

class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     
        #botones
        self.ui.Bcargar.clicked.connect(self.cargarimagen)
        self.ui.Bguardar.clicked.connect(self.guardarimagen)     
                
    def cargarimagen(self):
        global fileName, img
        global height, width, channels                    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog      
        fileName, _ = QFileDialog.getOpenFileName(self,"Seleccionar imagen", "","All Files (*);;Python Files (*.py)", options=options)      
        if fileName:
            img = cv2.imread(str(fileName))
            height, width, channels = img.shape
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)           
            img1=QtGui.QImage(img, width, height, QtGui.QImage.Format_RGB888)
            img2=QtGui.QPixmap.fromImage(img1)                
            self.ui.imoriginal.setPixmap(img2) 
               
        
    def guardarimagen(self):
        lum = float(self.ui.L1.text())
        sat = float(self.ui.C1.text())               
        #convierte RGB-YIQ-RGB 
        global nR, bG, nB
        global newimg, saveimg      
        newimg = img
        saveimg = img
        for w in range(width):
            for h in range(height):
                r1, g1, b1 = tuple(img[h][w]) 
                #yiq = colorsys.rgb_to_yiq(r, g, b) OK 
                y1 = 0.299*r1 + 0.587*g1 + 0.114*b1
                i1 = 0.595716*r1 - 0.274453*g1 - 0.321263*b1
                q1 = 0.211456*r1 - 0.522591*g1 + 0.311135*b1                                                  
                #yiq alterada
                y2 = y1*lum
                i2 = i1*sat
                q2 = q1*sat                    
                #convierte de yiq a rgb
                r2 = int(y2 + 0.948262*i2 + 0.624013*q2)
                g2 = int(y2 - 0.276066*i2 - 0.639810*q2)
                b2 = int(y2 - 1.105450*i2 + 1.729860*q2)                              
                #nueva img                                                                                                              
                newimg[h, w] = [r2, g2, b2]
                saveimg[h, w] = [r2, g2, b2]                
        #guarda la img nueva
        cv2.cvtColor(saveimg, cv2.COLOR_BGR2RGB, saveimg)   
        cv2.imwrite('newimage.png', saveimg)
        #pinta la img nueva
        cv2.cvtColor(newimg, cv2.COLOR_BGR2RGB, newimg)   
        img3=QtGui.QImage(newimg, width, height, QtGui.QImage.Format_RGB888)
        img4=QtGui.QPixmap.fromImage(img3)                 
        self.ui.improcesada.setPixmap(img4) 
                    
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())