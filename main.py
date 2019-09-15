# -*- coding: utf-8 -*-
#!/usr/bin/python3
from PyQt5 import QtWidgets
from bash import bash
import sys
from view import mainWindow
from model import model

def render():
    bash("pyuic5 view/template/mainWindow.ui -o view/template/tmainWindow.py")
render()

test = model.adb()

print(test.deviceList)
print(len(test.deviceList))

app = QtWidgets.QApplication([])
application = mainWindow.mainWindow()
application.show()
sys.exit(app.exec())