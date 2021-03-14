#!/usr/bin/python3
import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QUrl
import main_view

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(320,240)
    window.show()

    app.setApplicationDisplayName('Example App')
    app.setApplicationName('Example Applciation')
    app.setApplicationVersion('1.0.0')
    engine = QQmlApplicationEngine(QUrl("qrc:/qml/view.qml"),window)
    app.exec_()

