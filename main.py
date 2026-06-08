import pygame
from src.models.bola import bola
from src.services.audio_manager import AudioManager
from glob import glob
import random

pygame.init()

audio_files = glob('assets/audios/*.wav')
print("Arquivos encontrados: ", audio_files)

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

lista_bolas = []
for i in range(10):
    cor_aleatoria = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    nova_bola = bola( position_x = random.randint(100,700), position_y = random.randint(100, 500), raio = random.randint(10, 30), cor_hex = cor_aleatoria)
    nova_bola._vel_x = random.choice([-4, -5 , 4, 5])
    nova_bola._vel_y = random.choice([-4,-5 , 4, 5])
    lista_bolas.append(nova_bola)




manager = AudioManager(audio_files)
manager.load_audio(0)
manager.play(0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ritmo = manager.get_beat_multiplier()
    amp = manager.get_current_amplitude()
    
    screen.fill((0,0,0)) 
    
    for b in lista_bolas:
        b.update(amp, ritmo)
        b.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
       
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()