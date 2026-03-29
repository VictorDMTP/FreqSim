import pygame

class Particula:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tamanho = 10
        self.cor = (255,255,255)

    def desenhar(self , tela):
        pygame.draw.circle(tela, self.cor,(self.x, self.y), self.tamanho)
        pass