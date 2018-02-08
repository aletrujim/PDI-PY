from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        
        self.Bimg = QtWidgets.QPushButton(self.centralWidget)
        self.Bimg.setGeometry(QtCore.QRect(30, 20, 120, 23))
        self.Bimg.setObjectName("Bimg")     
        self.Bhis1 = QtWidgets.QPushButton(self.centralWidget)
        self.Bhis1.setGeometry(QtCore.QRect(150, 20, 120, 23))
        self.Bhis1.setObjectName("Bhis1")    
        self.CBfil = QtWidgets.QComboBox(self.centralWidget)
        self.CBfil.setGeometry(QtCore.QRect(600, 20, 150, 23))
        self.CBfil.setObjectName("CBfil")
        self.Bhis2 = QtWidgets.QPushButton(self.centralWidget)
        self.Bhis2.setGeometry(QtCore.QRect(750, 20, 120, 23))
        self.Bhis2.setObjectName("Bhis2")    
        
        self.img1 = QtWidgets.QLabel(self.centralWidget)
        self.img1.setGeometry(QtCore.QRect(30, 90, 500, 300))
        self.img1.setText("")
        self.img1.setObjectName("img1")        
        self.img2 = QtWidgets.QLabel(self.centralWidget)
        self.img2.setGeometry(QtCore.QRect(600, 90, 500, 300))
        self.img2.setText("")
        self.img2.setObjectName("img2")        
        
        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(30, 60, 100, 16))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(600, 60, 100, 16))
        self.label2.setObjectName("label2")
              
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Bimg.setText(_translate("MainWindow", "Imagen")) 
        self.Bhis1.setText(_translate("MainWindow", "Histograma"))
        self.Bhis2.setText(_translate("MainWindow", "Histograma"))
        self.label1.setText(_translate("MainWindow", "Imagen:"))
        self.label2.setText(_translate("MainWindow", "Imagen filtrada:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


