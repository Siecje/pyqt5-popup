import sys
from PyQt5 import QtGui, QtQml

app = QtGui.QGuiApplication(sys.argv)
engine = QtQml.QQmlApplicationEngine("main.qml")
app.exec_()
