from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap

class MapViewer(QLabel):
    def __init__(self, parentWin, x,y,w,h):
        super(MapViewer, self).__init__(parentWin)
        self.setGeometry(x,y,w,h)
        self.parent = parentWin
        
class RoomViewer(QLabel):
    def __init__(self, parentWin, x,y,w,h):
        super(RoomViewer, self).__init__(parentWin)
        self.setGeometry(x,y,w,h)
        self.setPixmap(QPixmap("assets/rooms/swamp.jpg").scaled(w,h))
        self.parent = parentWin