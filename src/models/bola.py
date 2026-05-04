from src.models.base_entity import VisualEntity
import pygame

class bola(VisualEntity):
    def __init__(self,position_x, position_y, cor_hex, raio: int):
        super().__init__(position_x, position_y, cor_hex)
        self._raio_base = raio 
        self._raio = raio
        self._vel_x = 5
        self._vel_y = 5
        
    def draw(self, screen):
        pygame.draw.circle(screen, self._cor_hex,(self._position_x, self._position_y),self._raio)
    
    def update(self, data):
        self._raio = self._raio_base + (abs(data) * 150) 
        fator_velocidade = 1 + (abs(data) * 10)
        
        self._position_x += self._vel_x * fator_velocidade
        self._position_y += self._vel_y * fator_velocidade
        
        if self._position_x - self._raio <= 0:
            self._position_x = self._raio
            self._vel_x *= -1
            
        elif self._position_x + self._raio >= 800:
            self._position_x = 800 - self._raio
            self._vel_x *= -1
        
        if self._position_y - self._raio <= 0:
            self._position_y = self._raio
            self._vel_y *= -1
        elif self._position_y + self._raio >= 600:
            self._position_y = 600 - self._raio
            self._vel_y *= -1
            