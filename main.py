import pygame
from src.models.bola import bola
from src.services.audio_manager import AudioManager
from glob import glob
from src.repositories.BolaRepository import BolaRepository
import random

pygame.init()

audio_files = glob('assets/audios/*.wav')
print("Arquivos encontrados: ", audio_files)

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

repo = BolaRepository()
dados_salvos = repo.carregar()

lista_bolas = []

if dados_salvos:
    for d in dados_salvos:
        nova_bola = bola(
            position_x=d['x'],
            position_y=d['y'],
            cor_hex=(0,0,0),
            raio=d['raio']
        )
        nova_bola._vel_x = d['vel_x']
        nova_bola._vel_y = d['vel_y']
        nova_bola._matiz_base = d['matiz']
        lista_bolas.append(nova_bola)
else:
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
            repo.salvar(lista_bolas)
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