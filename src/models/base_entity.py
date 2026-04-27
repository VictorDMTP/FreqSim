from abc import ABC, abstractmethod

class VisualEntity(ABC):
    def __init__(self, position_x: int , position_y: int , cor_hex):
        self._position_x = position_x
        self._position_y = position_y
        self._cor_hex = cor_hex

    @abstractmethod
    def update(self, data):
        pass
        
    @abstractmethod    
    def draw(self, screen):
        pass