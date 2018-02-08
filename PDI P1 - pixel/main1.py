import sys
import cv2 #opencv

from novogui1 import Ui_MainWindow

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog

class Main(QMainWindow):        
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)                       
        #botones
        self.ui.Carregar.clicked.connect(self.carregarimagen)
        self.ui.Salvar.clicked.connect(self.salvarimagen) 
    
    def carregarimagen(self):
        global fileName, img 
        global height, width, channels       
        #buscador
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog      
        fileName, _ = QFileDialog.getOpenFileName(self,"Seleccionar imagen", "","All Files (*);;Python Files (*.py)", options=options)
        
        if fileName:
            #cargar imagen       
            img = cv2.imread(str(fileName))           
            #tamano de la imagen
            height, width, channels = img.shape        
            #convierte la img a RGB
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)           
            #pinta la imag en el label
            img=QtGui.QImage(img, width, height, QtGui.QImage.Format_RGB888)
            img=QtGui.QPixmap.fromImage(img)                
            self.ui.ImagemOri.setPixmap(img) 
                   
    def salvarimagen(self):        
        #cargar imagen original
        img = cv2.imread(fileName)        
        #leer rango pixels       
        x1 = int(self.ui.X1.text())
        x2 = int(self.ui.X2.text())
        y1 = int(self.ui.Y1.text())
        y2 = int(self.ui.Y2.text())        
        #leer nueva color       
        c1 = int(self.ui.C1.text())
        c2 = int(self.ui.C2.text())
        c3 = int(self.ui.C3.text())             
        #cambia color pixel
        img[x1:x2, y1:y2] = [c1, c2, c3]
        #guarda la img nueva
        cv2.imwrite('newimage.png', img)      
        #pinta la img nueva
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)   
        img2=QtGui.QImage(img, width, height, QtGui.QImage.Format_RGB888)
        img2=QtGui.QPixmap.fromImage(img2)   
        self.ui.ImagemOri.setPixmap(img2)          
                   
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
    
