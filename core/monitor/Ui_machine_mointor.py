# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\eric6_workspace\PyQt5-pyserial\monitor/machine_mointor.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(806, 448)
        Dialog.setSizeGripEnabled(True)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 521, 331))
        self.groupBox.setObjectName("groupBox")
        self.yAxisup = QtWidgets.QPushButton(self.groupBox)
        self.yAxisup.setGeometry(QtCore.QRect(120, 20, 91, 61))
        self.yAxisup.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/arrow-up-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yAxisup.setIcon(icon)
        self.yAxisup.setIconSize(QtCore.QSize(30, 30))
        self.yAxisup.setObjectName("yAxisup")
        self.xAxisleft = QtWidgets.QPushButton(self.groupBox)
        self.xAxisleft.setGeometry(QtCore.QRect(0, 110, 91, 61))
        self.xAxisleft.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icon/arrow-left-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xAxisleft.setIcon(icon1)
        self.xAxisleft.setIconSize(QtCore.QSize(30, 30))
        self.xAxisleft.setObjectName("xAxisleft")
        self.xAxisrigh = QtWidgets.QPushButton(self.groupBox)
        self.xAxisrigh.setGeometry(QtCore.QRect(230, 110, 91, 61))
        self.xAxisrigh.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icon/arrow-right-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xAxisrigh.setIcon(icon2)
        self.xAxisrigh.setIconSize(QtCore.QSize(30, 30))
        self.xAxisrigh.setObjectName("xAxisrigh")
        self.yAxisdown = QtWidgets.QPushButton(self.groupBox)
        self.yAxisdown.setGeometry(QtCore.QRect(120, 190, 91, 61))
        self.yAxisdown.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icon/arrow-down-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yAxisdown.setIcon(icon3)
        self.yAxisdown.setIconSize(QtCore.QSize(30, 30))
        self.yAxisdown.setObjectName("yAxisdown")
        self.zupButton = QtWidgets.QPushButton(self.groupBox)
        self.zupButton.setGeometry(QtCore.QRect(380, 20, 91, 61))
        self.zupButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icon/arrow-up-a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zupButton.setIcon(icon4)
        self.zupButton.setIconSize(QtCore.QSize(30, 30))
        self.zupButton.setObjectName("zupButton")
        self.zdownButton = QtWidgets.QPushButton(self.groupBox)
        self.zdownButton.setGeometry(QtCore.QRect(380, 220, 91, 51))
        self.zdownButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../icon/arrow-down-a.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zdownButton.setIcon(icon5)
        self.zdownButton.setIconSize(QtCore.QSize(30, 30))
        self.zdownButton.setObjectName("zdownButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(380, 130, 81, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.unlockMachine = QtWidgets.QPushButton(self.groupBox)
        self.unlockMachine.setGeometry(QtCore.QRect(10, 290, 101, 31))
        self.unlockMachine.setObjectName("unlockMachine")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(140, 130, 51, 21))
        self.label_2.setObjectName("label_2")
        self.homeButton = QtWidgets.QPushButton(self.groupBox)
        self.homeButton.setGeometry(QtCore.QRect(130, 290, 91, 31))
        self.homeButton.setObjectName("homeButton")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(560, 40, 211, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.xAxis = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.xAxis.setObjectName("xAxis")
        self.gridLayout.addWidget(self.xAxis, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.yAxis = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.yAxis.setObjectName("yAxis")
        self.gridLayout.addWidget(self.yAxis, 1, 1, 1, 1)
        self.zAxis = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.zAxis.setObjectName("zAxis")
        self.gridLayout.addWidget(self.zAxis, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Axis Adjust"))
        self.label.setText(_translate("Dialog", "Z jog"))
        self.unlockMachine.setText(_translate("Dialog", "Unlock machine"))
        self.label_2.setText(_translate("Dialog", "X-Y Axis"))
        self.homeButton.setText(_translate("Dialog", "Home"))
        self.label_3.setText(_translate("Dialog", "X"))
        self.label_4.setText(_translate("Dialog", "Y"))
        self.label_5.setText(_translate("Dialog", "Z"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

