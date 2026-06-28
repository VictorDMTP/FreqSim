from src.models.base_entity import VisualEntity
import pygame
import random

class bola(VisualEntity):
    def __init__(self, position_x, position_y, cor_hex, raio: int, frequencia_idx: int):
        super().__init__(position_x, position_y, cor_hex)
        self._raio = raio 
        self._y_base = position_y
        self._matiz_base = random.randint(0, 360)
        self._frequencia_idx = frequencia_idx
        
    def draw(self, screen):
        pygame.draw.circle(screen, self._cor_hex, (int(self._position_x), int(self._position_y)), int(self._raio))
    
    def update(self, data, multiplicador_ritmo=1.0): 
        if multiplicador_ritmo > 1.0:
            self._matiz_base = random.randint(0, 360) 
        
        cor_temp = pygame.Color(0)
        cor_temp.hsva = (self._matiz_base, 100, 100, 100)
        self._cor_hex = (cor_temp.r, cor_temp.g, cor_temp.b)

    
        if isinstance(data, list) and self._frequencia_idx < len(data):
            dado_som = data[self._frequencia_idx]
        else:
            dado_som = 0

        multiplicador_sensibilidade = 40 + (self._frequencia_idx * 22)
        
        teto_maximo = 250
        
        altura_alvo = self._y_base - (abs(dado_som) * multiplicador_sensibilidade)
        altura_alvo = max(teto_maximo, min(self._y_base, altura_alvo))
        
    
        self._position_y += (altura_alvo - self._position_y) * 0.25