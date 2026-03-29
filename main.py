import pygame
import sys

def principal():
    pygame.init()
    tela = pygame.display.set_mode((800,600))
    pygame.display.set_caption("FreqSim")
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
        tela.fill((0,0, 0))
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    principal()