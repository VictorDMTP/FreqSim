import pygame
from src.models.bola import bola
from src.services.audio_manager import AudioManager
from glob import glob
from src.repositories.BolaRepository import BolaRepository
import random

pygame.init()

audio_files = glob('assets/audios/*.wav')
print("Arquivos encontrados: ", audio_files)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

repo = BolaRepository()
dados_salvos = repo.carregar()

lista_bolas = []

if dados_salvos:
    for d in dados_salvos:
        nova_bola = bola(
            position_x=d['x'],
            position_y=d['y'],
            cor_hex=(0, 0, 0),
            raio=d['raio']
        )
        nova_bola._vel_x = d['vel_x']
        nova_bola._vel_y = d['vel_y']
        nova_bola._matiz_base = d['matiz']
        lista_bolas.append(nova_bola)
else:
    for i in range(10):
         cor_aleatoria = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
         nova_bola = bola(position_x=random.randint(100, 700), position_y=random.randint(100, 500), raio=random.randint(10, 30), cor_hex=cor_aleatoria)
         
         nova_bola._vel_x = random.choice([-4, -5, 4, 5]) 
         nova_bola._vel_y = random.choice([-4, -5, 4, 5]) 
         lista_bolas.append(nova_bola)

manager = AudioManager(audio_files)

indice_musica = 0
pausado = True

manager.load_audio(indice_musica)
manager.play(indice_musica)
pygame.mixer.music.pause()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            repo.salvar(lista_bolas)
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pausado = not pausado
                if pausado:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            
            elif event.key == pygame.K_RIGHT:
                if len(audio_files) > 0:
                    indice_musica = (indice_musica + 1) % len(audio_files)
                    manager.load_audio(indice_musica)
                    manager.play(indice_musica)
                    if pausado:
                        pygame.mixer.music.pause()
            elif event.key == pygame.K_LEFT:
                if len(audio_files) > 0:
                    indice_musica = (indice_musica - 1) % len(audio_files)
                    manager.load_audio(indice_musica)
                    manager.play(indice_musica)
                    if pausado:
                        pygame.mixer.music.pause()
            
    ritmo = manager.get_beat_multiplier()
    amp = manager.get_current_amplitude()
    
    screen.fill((0, 0, 0)) 
    
    for b in lista_bolas:
        if not pausado:
            b.update(amp, ritmo)
            
        b.draw(screen)
        
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()