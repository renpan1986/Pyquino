# -*- coding: utf-8 -*-

"""
Module implementing Machine.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_machine_mointor import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
#from mainwindow import MainWindow
import serialportcontext


class Machine(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Machine, self).__init__(parent)
        self.setupUi(self)
        #self.initdaForms()
        
        
        
   # def initdaForms(self):
        
        #self.homeButton.clicked.connect(self.__test__send)
        
    def __test__send(self):
        data = str("G29"+'\n')
        print(data)
        if self._serial_context_.isRunning():
            if len(data) > 0:
                self._serial_context_.send(data, 0)
                print(data)
    

#    def __run__(self):
 #       import sys
  #      print("123")
  #      app = QtWidgets.QApplication(sys.argv)
  #      Dialog = QtWidgets.QDialog()
  #      ui = Ui_Dialog()
  #      ui.setupUi(Dialog)
  #      Dialog.show()
  #       sys.exit(app.exec_())
    
    @pyqtSlot()
    def on_homeButton_clicked(self):
        print("test the button")
        #self.__test__send()
        raise NotImplementedError
    

