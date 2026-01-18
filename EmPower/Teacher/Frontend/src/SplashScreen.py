import time
import os

from PyQt5.QtWidgets import QSplashScreen, QProgressBar
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        ui_path = "Frontend/PyQT_UI/splash.ui"
        if os.path.exists(ui_path):
            loadUi(ui_path, self)
            self.setWindowFlag(Qt.FramelessWindowHint)
        else:
            # Fallback: create a minimal progress bar so startup can proceed without the .ui file
            self.setFixedSize(480, 180)
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setStyleSheet('''
               QSplashScreen {
                   background-color: rgba(1,42,89,1);
                   background-position: center;
                   border-radius: 15px;
               }
           ''')
            # create a simple progressBar attribute expected by other code
            self.progressBar = QProgressBar(self)
            self.progressBar.setGeometry(40, 120, 400, 20)
            self.progressBar.setRange(0, 100)
            self.progressBar.setValue(0)
        # If the UI file was loaded it already has styling; otherwise the fallback creates
        # a simple progressBar. Try to customize the progressBar style if present.
        try:
            self.progressBar.setStyleSheet('''
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    background-color: #f0f0f0;
                    text-align: center;
                }

                QProgressBar::chunk {
                    background-color: #52b29f;
                    width: 8px;
                }
            ''')
        except Exception:
            pass

    def progress(self):
        for i in range(100):
            time.sleep(0.0125)
            self.progressBar.setValue(i)
