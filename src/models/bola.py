from src.models.base_entity import VisualEntity
import pygame
import random

class bola(VisualEntity):
    def __init__(self, position_x, position_y, cor_hex, raio: int):
        super().__init__(position_x, position_y, cor_hex)
        self._raio_base = raio 
        self._raio = raio
        self._vel_x = 5
        self._vel_y = 5
        self._matiz_base = random.randint(0, 360)
        
    def draw(self, screen):
        pygame.draw.circle(screen, self._cor_hex, (int(self._position_x), int(self._position_y)), int(self._raio))
    
    def update(self, data, multiplicador_ritmo=1.0):
        self._raio = self._raio_base + (abs(data) * 30) 

        fator_velocidade = 1 * multiplicador_ritmo

        if multiplicador_ritmo > 1.0:
            self._matiz_base = (self._matiz_base + 15) % 360
        
        cor_temp = pygame.Color(0)
        cor_temp.hsva = (self._matiz_base, 100, 100, 100)
        self._cor_hex = (cor_temp.r, cor_temp.g, cor_temp.b)

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