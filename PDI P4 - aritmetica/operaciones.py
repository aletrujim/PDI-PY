import sys
import cv2 
from gui4 import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog

class Main(QMainWindow):        
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)                       
        self.ui.Bimg1.clicked.connect(self.Bimg1)
        self.ui.Bimg2.clicked.connect(self.Bimg2)      
        self.ui.CBopera.activated.connect(self.CBopera)              
        self.ui.CBopera.addItems(['Escoger operacion', 'RGB Suma promedio', 'RGB Suma clampeada', 'RGB Resta promedio', 'RGB Resta clampeada', 
                                  'YIQ Suma promedio', 'YIQ Suma clampeada', 'YIQ Resta promedio', 'YIQ Resta clampeada', 
                                  'YIQ If ligther', 'YIQ If darker'])
        
    def Bimg1(self):
        global fileName1, img1
        global height1, width1        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog      
        fileName1, _ = QFileDialog.getOpenFileName(self,"Seleccionar imagen", "", filter='Imagen (*.png *.jpg *.bmp)', options=options)       
        if fileName1:
            img1 = cv2.imread(str(fileName1))           
            height1, width1, ch1 = img1.shape     
            img1r=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)           
            img1i=QtGui.QImage(img1r, width1, height1, QtGui.QImage.Format_RGB888)
            img1p=QtGui.QPixmap.fromImage(img1i)                
            self.ui.img1.setPixmap(img1p) 
            
    def Bimg2(self):
        global fileName2, img2
        global height2, width2       
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog      
        fileName2, _ = QFileDialog.getOpenFileName(self,"Seleccionar imagen", "",filter='Imagen (*.png *.jpg *.bmp)', options=options)        
        if fileName2:
            img2 = cv2.imread(str(fileName2))
            #height2, width2, ch2 = img1.shape
            height2 = height1
            width2 = width1
                      
            img2r=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)           
            img2i=QtGui.QImage(img2r, width2, height2, QtGui.QImage.Format_RGB888)
            img2p=QtGui.QPixmap.fromImage(img2i)                
            self.ui.img2.setPixmap(img2p) 
            
    def CBopera(self):        
        opera = str(self.ui.CBopera.currentText())
                
        img3 = 0
                
        if opera == 'RGB Suma promedio':
            img3 = (img1 + img2)/2
                
        elif opera == 'RGB Suma clampeada':
            img3 = img1 + img2
            img3[img3[:,:,0]>255] = 255
            img3[img3[:,:,1]>255] = 255
            img3[img3[:,:,2]>255] = 255
                
        elif opera == 'RGB Resta promedio':
            img3 = (img1 - img2)/2
                
        elif opera == 'RGB Resta clampeada':
            img3 = img1 - img2           
            img3[img3[:,:,0]<0] = 0
            img3[img3[:,:,1]<0] = 0
            img3[img3[:,:,2]<0] = 0
                
        elif opera == 'YIQ Suma promedio':
            yiq_img1 = rgb_yiq(img1, width1, height1)
            yiq_img2 = rgb_yiq(img2, width2, height2)            
            yiq_img3 = (yiq_img1 + yiq_img2)/2           
            height3, width3, ch3 = yiq_img3.shape
            img3 = yiq_rgb(yiq_img3, width3, height3)                                    
            
        elif opera == 'YIQ Suma clampeada':
            yiq_img1 = rgb_yiq(img1, width1, height1)
            yiq_img2 = rgb_yiq(img2, width2, height2)            
            yiq_img3 = yiq_img1 + yiq_img2         
            height3, width3, ch3 = yiq_img3.shape
            img3 = yiq_rgb(yiq_img3, width3, height3)                                    
            img3[img3[:,:,0]>255] = 255
            img3[img3[:,:,1]>255] = 255
            img3[img3[:,:,2]>255] = 255
            
        elif opera == 'YIQ Resta promedio':
            yiq_img1 = rgb_yiq(img1, width1, height1)
            yiq_img2 = rgb_yiq(img2, width2, height2)            
            yiq_img3 = (yiq_img1 - yiq_img2)/2           
            height3, width3, ch3 = yiq_img3.shape
            img3 = yiq_rgb(yiq_img3, width3, height3)                                    
            
        elif opera == 'YIQ Resta clampeada':
            yiq_img1 = rgb_yiq(img1, width1, height1)
            yiq_img2 = rgb_yiq(img2, width2, height2)            
            yiq_img3 = yiq_img1 - yiq_img2         
            height3, width3, ch3 = yiq_img3.shape
            img3 = yiq_rgb(yiq_img3, width3, height3)                                    
            img3[img3[:,:,0]>255] = 255
            img3[img3[:,:,1]>255] = 255
            img3[img3[:,:,2]>255] = 255
            
        elif opera == 'YIQ If ligther':
            yiq_img1 = rgb_yiq(img1, width1, height1)
            yiq_img2 = rgb_yiq(img2, width2, height2)     
           
            yiq_img3 = yiq_img1
            for w in range(width1):
                for h in range(height1):
                    y1, i1, q1 = tuple(yiq_img1[h][w])
                    y2, i2, q2 = tuple(yiq_img2[h][w])
                    if y1 >= y2:
                        y = y1
                        i = i1
                        q = q1
                    elif y1 < y2:
                        y = y2
                        i = i2
                        q = q2
                    yiq_img3[h, w] = [y, i, q]
            
            height3, width3, ch3 = yiq_img3.shape
            img3 = yiq_rgb(yiq_img3, width3, height3)                                    
            img3[img3[:,:,0]>255] = 255
            img3[img3[:,:,1]>255] = 255
            img3[img3[:,:,2]>255] = 255
            
        elif opera == 'YIQ If darker':
            yiq_img1 = rgb_yiq(img1, width1, height1)
            yiq_img2 = rgb_yiq(img2, width2, height2)     
           
            yiq_img3 = yiq_img1
            for w in range(width1):
                for h in range(height1):
                    y1, i1, q1 = tuple(yiq_img1[h][w])
                    y2, i2, q2 = tuple(yiq_img2[h][w])
                    if y1 <= y2:
                        y = y1
                        i = i1
                        q = q1
                    elif y1 > y2:
                        y = y2
                        i = i2
                        q = q2
                    yiq_img3[h, w] = [y, i, q]
            
            height3, width3, ch3 = yiq_img3.shape
            img3 = yiq_rgb(yiq_img3, width3, height3)                                    
            img3[img3[:,:,0]>255] = 255
            img3[img3[:,:,1]>255] = 255
            img3[img3[:,:,2]>255] = 255
  
        cv2.imwrite('newimage.png', img3)    
        height3, width3, channels3 = img3.shape
        imgr = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)   
        imgri=QtGui.QImage(imgr, width3, height3, QtGui.QImage.Format_RGB888)
        imgrp=QtGui.QPixmap.fromImage(imgri) 
        
        self.ui.img3.setPixmap(imgrp)
               
def rgb_yiq(img, width, height):       
    yiq_img = img
    for w in range(width):
        for h in range(height):
            r, g, b = tuple(img[h][w]) 
            y = 0.299*r + 0.587*g + 0.114*b
            i = 0.595716*r - 0.274453*g - 0.321263*b
            q = 0.211456*r - 0.522591*g + 0.311135*b                                                   
            yiq_img[h, w] = [y, i, q]
    return yiq_img

def yiq_rgb(img, width, height):
    rgb_img = img
    for w in range(width):
        for h in range(height):
            y, i, q = tuple(img[h][w]) 
            r = y + 0.948262*i + 0.624013*q
            g = y - 0.276066*i - 0.639810*q
            b = y - 1.105450*i + 1.729860*q                                               
            rgb_img[h, w] = [r, g, b]
    return rgb_img
   

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())