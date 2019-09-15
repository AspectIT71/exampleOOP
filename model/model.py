from PyQt5.QtWidgets import QFileDialog, QMessageBox
from bash import bash
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer
import sys,os
import datetime
from view.template import tMainWindow
from view.template.tMainWindow import Ui_MainWindow
ADB_FILE = "./resourses/adb"


class adb():

    def __init__(self):
        self.deviceList = self.getDeviceList()
        self.currentDevice = ''

    def getDeviceList(self):
         deviceOutput = str(bash(ADB_FILE + " devices -l")).splitlines()[1:]
         arrDevices = []
         for device in range(len(deviceOutput)):
            arrDevices.append(deviceOutput[device].split())
         return arrDevices

    def checkConnectDevice(self):
        if not self.getDeviceList() or []:
             return 0
        else:
             return 1

    def setCurrentDevice(self, device):
         self.currentDevice = device

    def getCurentDevice(self):
        return self.currentDevice

    def install(self, path):
        bash('adb -s ' + str(self.deviceList[self.currentDevice][0]) + ' install -r -d ' + path)
