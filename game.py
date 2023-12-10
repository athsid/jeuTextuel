from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel
from PySide6.QtGui import QIcon, QPixmap
import sys

from graphics import *

        

class Window(QMainWindow):
    
    def __init__(self):
        """initialise la fenetre"""
        super(Window, self).__init__()
        self.setUI()
    
    def setUI(self):
        """met en place l'interface graphique du jeu"""
        self.setWindowTitle("JEU")
        self.setWindowIcon(QIcon())
        self.setFixedSize(1920,1080)
        self.setStyleSheet("background-color: #2E3440")
        
        self.mapViewer = MapViewer(self, 970,20,930,510)
        """QWidget(self)
        self.mapViewer.setGeometry(970,20,930,510)
        self.mapViewer.setStyleSheet("background-color: green;")"""
        
        self.roomViewer = QWidget(self)
        self.roomViewer.setGeometry(20,20,930,510)
        self.roomViewer.setStyleSheet("background-color: red;")
        
        self.itemViewer = QWidget(self)
        self.itemViewer.setGeometry(970,550,930,510)
        self.itemViewer.setStyleSheet("background-color: yellow;")
        
        self.textViewer = QWidget(self)
        self.textViewer.setGeometry(20,550,930,510)
        self.textViewer.setStyleSheet("background-color: grey;")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())