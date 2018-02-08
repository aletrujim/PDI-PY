# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 449)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Bcargar = QtWidgets.QPushButton(self.centralWidget)
        self.Bcargar.setGeometry(QtCore.QRect(30, 20, 121, 23))
        self.Bcargar.setObjectName("Bcargar")
        self.imoriginal = QtWidgets.QLabel(self.centralWidget)
        self.imoriginal.setGeometry(QtCore.QRect(30, 90, 211, 171))
        self.imoriginal.setText("")
        self.imoriginal.setObjectName("imoriginal")
        self.improcesada = QtWidgets.QLabel(self.centralWidget)
        self.improcesada.setGeometry(QtCore.QRect(300, 90, 211, 171))
        self.improcesada.setText("")
        self.improcesada.setObjectName("improcesada")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(290, 60, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(30, 280, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(30, 340, 171, 16))
        self.label_4.setObjectName("label_4")
        self.Bguardar = QtWidgets.QPushButton(self.centralWidget)
        self.Bguardar.setGeometry(QtCore.QRect(290, 20, 121, 23))
        self.Bguardar.setObjectName("Bguardar")
        self.L1 = QtWidgets.QLineEdit(self.centralWidget)
        self.L1.setGeometry(QtCore.QRect(120, 280, 61, 20))
        self.L1.setObjectName("L1")
        self.C1 = QtWidgets.QLineEdit(self.centralWidget)
        self.C1.setGeometry(QtCore.QRect(200, 340, 61, 20))
        self.C1.setObjectName("C1")
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
        self.Bcargar.setText(_translate("MainWindow", "Cargar Imagen")) 
        self.L1.setText(_translate("MainWindow", "1"))
        self.C1.setText(_translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "Imagen Original:"))
        self.label_2.setText(_translate("MainWindow", "Imagen Procesada:"))
        self.label_3.setText(_translate("MainWindow", "Luminancia:   alfa:"))
        self.label_4.setText(_translate("MainWindow", "Cromaticidad (Saturación):   beta:"))
        self.Bguardar.setText(_translate("MainWindow", "Procesar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

