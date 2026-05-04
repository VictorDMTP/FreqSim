import pygame
from src.models.bola import bola
from src.services.audio_manager import AudioManager
from glob import glob

pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

bola: bola = bola(200, 300, (255,0,0), 20)

audio_files = glob('assets/audio/*.wav')

manager = AudioManager(audio_files)
manager.load_audio(0)
manager.play(0)

running = True
while running:
    
    amp = manager.get_current_amplitude()
    
    bola.update(amp)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0,0,0))         
            
    bola.draw(screen)
       
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()