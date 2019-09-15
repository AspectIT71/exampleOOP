from PyQt5.QtWidgets import QFileDialog, QMessageBox
from bash import bash
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer
import sys,os
import datetime
from view.template import tMainWindow
from view.template.tMainWindow import Ui_MainWindow
from model import model


class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.adb = model.adb()
        self.renderDeviceList()
        self.updateDeviceList()
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.comboBox.currentIndexChanged.connect(self.handleActivated)
        self.defaultDevice()

    def defaultDevice(self):
        self.adb.setCurrentDevice(self.ui.comboBox.currentIndex())

    def btnClicked(self):
        filePath = QFileDialog.getOpenFileName(self, "Открыть", os.path.expanduser("~/Documents"), "*.apk")
        self.adb.install(filePath[0])

    def handleActivated(self, index):
        self.adb.setCurrentDevice(index)

    def renderDeviceList(self):
        self.currentDeviceList = self.adb.getDeviceList()
        for device in self.currentDeviceList:
            self.ui.comboBox.addItem(device[4])
            self.adb.device = self.currentDeviceList

    def updateDeviceList(self):
        if  self.adb.getDeviceList() != self.currentDeviceList:
            self.ui.comboBox.clear()
            self.renderDeviceList()
        else:
            pass
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDeviceList)
        self.timer.start(500)

        print(self.adb.currentDevice)





