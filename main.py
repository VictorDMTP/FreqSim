import pygame
from src.models.bolinha import bolinha

pygame.init()

screen = pygame.display.set_mode((640,640))
clock = pygame.time.Clock()

bola1: bolinha = bolinha(200, 300, (255,0,0), 20)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0,0,0))         
            
    bola1.draw(screen)
       
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()