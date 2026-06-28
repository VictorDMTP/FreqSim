import pygame
import random

class Particula:
    def __init__(self, largura_tela):
        self._largura_tela = largura_tela
        self.reset()

    def reset(self):
        self._x = random.randint(100, self._largura_tela - 100)
        self._y = -20
        self._raio = 10  
        self._vel_y = 0
        self._vel_x = 0
        self._gravidade = 0.4
        self._cor = (255, 255, 255)  

    def draw(self, screen):
        pygame.draw.circle(screen, self._cor, (int(self._x), int(self._y)), self._raio)

    def update(self, lista_bolas, altura_tela):
       
        self._vel_y += self._gravidade
        self._x += self._vel_x
        self._y += self._vel_y
        self._vel_x *= 0.95

        num_bolas = len(lista_bolas)
        if num_bolas > 1:
            espacamento = (self._largura_tela - 160) / (num_bolas - 1)
            
           
            idx = int((self._x - 80) / espacamento)
            
            if 0 <= idx < num_bolas - 1:
                b1 = lista_bolas[idx]
                b2 = lista_bolas[idx + 1]
                
               
                t = (self._x - b1._position_x) / espacamento
                altura_rampa = b1._position_y + t * (b2._position_y - b1._position_y)
                altura_superficie = altura_rampa - (self._raio + b1._raio)
                
               
                if self._y >= altura_superficie:
                    self._y = altura_superficie  
                    self._vel_y = 0              
                    
                   
                    inclinacao = (b2._position_y - b1._position_y) / espacamento
                    self._vel_x += inclinacao * 0.4  
            else:
                self._vel_y = max(self._vel_y, 4)

       
        if self._y > altura_tela + 20 or self._x < 0 or self._x > self._largura_tela:
            self.reset()