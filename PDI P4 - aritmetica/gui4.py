# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:21:41 2017

@author: ALEXA TRUJILLO
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 450)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        
        self.Bimg1 = QtWidgets.QPushButton(self.centralWidget)
        self.Bimg1.setGeometry(QtCore.QRect(30, 20, 120, 23))
        self.Bimg1.setObjectName("Bimg1")     
        self.Bimg2 = QtWidgets.QPushButton(self.centralWidget)
        self.Bimg2.setGeometry(QtCore.QRect(430, 20, 120, 23))
        self.Bimg2.setObjectName("Bimg2")        
        
        self.CBopera = QtWidgets.QComboBox(self.centralWidget)
        self.CBopera.setGeometry(QtCore.QRect(830, 20, 150, 23))
        self.CBopera.setObjectName("CBopera")
        
        self.img1 = QtWidgets.QLabel(self.centralWidget)
        self.img1.setGeometry(QtCore.QRect(30, 70, 350, 350))
        self.img1.setText("")
        self.img1.setObjectName("img1")        
        self.img2 = QtWidgets.QLabel(self.centralWidget)
        self.img2.setGeometry(QtCore.QRect(430, 70, 350, 350))
        self.img2.setText("")
        self.img2.setObjectName("img2")        
        self.img3 = QtWidgets.QLabel(self.centralWidget)
        self.img3.setGeometry(QtCore.QRect(830, 70, 350, 350))
        self.img3.setText("")
        self.img3.setObjectName("img3")
        
        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(30, 70, 100, 16))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(430, 70, 100, 16))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralWidget)
        self.label3.setGeometry(QtCore.QRect(830, 70, 100, 16))
        self.label3.setObjectName("label3")
              
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
        self.Bimg1.setText(_translate("MainWindow", "Imagen 1")) 
        self.Bimg2.setText(_translate("MainWindow", "Imagen 2"))
        self.label1.setText(_translate("MainWindow", "Imagen 1:"))
        self.label2.setText(_translate("MainWindow", "Imagen 2:"))
        self.label3.setText(_translate("MainWindow", "Imagen Resultante:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


