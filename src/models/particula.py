import pygame
import random

class Particula:
    def __init__(self, largura_tela):
        self._largura_tela = largura_tela
        self.reset()

    def reset(self):
        self._x = random.randint(100, self._largura_tela - 100)
        self._y = -20
        self._raio = 5  
        self._vel_y = 6
        self._vel_x = 0
        self._cor = (255, 215, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self._cor, (int(self._x), int(self._y)), self._raio)

    def update(self, lista_bolas, altura_tela):
        self._x += self._vel_x
        self._vel_x *= 0.90

        colidiu = False

        for b in lista_bolas:
            dx = self._x - b._position_x
            
            
            raio_combinado = self._raio + b._raio 
            
            if abs(dx) < raio_combinado:
                altura_superficie = b._position_y - (raio_combinado**2 - dx**2) ** 0.5
                
                if self._y >= altura_superficie - 150 and self._y <= b._position_y:
                    self._y = altura_superficie  
                    self._vel_y = 0
                    colidiu = True
                    
                    if dx < 0:
                        self._vel_x -= 0.6
                    else:
                        self._vel_x += 0.6
                    break

        if not colidiu:
            self._vel_y = 6
            self._y += self._vel_y

        if self._y > altura_tela + 20:
            self.reset()