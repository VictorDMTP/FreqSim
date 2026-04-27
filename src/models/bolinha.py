from src.models.base_entity import VisualEntity
import pygame

class bolinha(VisualEntity):
    def __init__(self,position_x,position_y,cor_hex,raio: int):
        super().__init__(position_x,position_y,cor_hex)
        self._raio = raio
        
    def draw(self, screen):
        pygame.draw.circle(screen, self._cor_hex,(self._position_x, self._position_y),self._raio)
    
    def update(self, data):
        pass