# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drawButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.drawButton.setGeometry(QtCore.QRect(350, 220, 113, 61))
        self.drawButton.setObjectName("drawButton")
        self.art = QtWidgets.QLabel(parent=self.centralwidget)
        self.art.setGeometry(QtCore.QRect(260, 280, 301, 71))
        self.art.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.art.setObjectName("art")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.drawButton.setText(_translate("MainWindow", "DRAW"))
        self.art.setText(_translate("MainWindow", "NOT DRAWING"))