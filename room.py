from PySide6.QtGui import QPixmap

class Room():
    def __init__(self, name: str, level: int, description: str, exits: dict(str, str)):
        
        self.image = QPixmap("assets/rooms/"+name+".jpg").scaled(930,510)
        self.level = level
        self.description = description
        
        self.exits = exits
        
    
    
        