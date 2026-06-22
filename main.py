import pygame
from src.models.bola import bola
from src.models.particula import Particula  
from src.services.audio_manager import AudioManager
from src.repositories.BolaRepository import BolaRepository  
from glob import glob
import random

pygame.init()
pygame.font.init()

audio_files = glob('assets/audios/*.wav')
print("Arquivos encontrados: ", audio_files)

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 22)

NUM_BOLAS = 100
espacamento = (1280 - 160) / (NUM_BOLAS - 1)

lista_bolas = []
for i in range(NUM_BOLAS):
    x_dinamico = 80 + (i * espacamento)
    cor_aleatoria = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
    
    nova_bola = bola(
        position_x=x_dinamico,
        position_y=650, 
        raio=4,
        cor_hex=cor_aleatoria,
        frequencia_idx=i
    ) 
    lista_bolas.append(nova_bola)

objeto_areia = Particula(1280) 
repo = BolaRepository()

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
            if len(audio_files) > 0:
                nome_limpo = audio_files[indice_musica].split('/')[-1].split('\\')[-1].replace('.wav', '')
                repo.salvar(f"historico_{nome_limpo}.json")
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
                    nome_limpo = audio_files[indice_musica].split('/')[-1].split('\\')[-1].replace('.wav', '')
                    repo.salvar(f"historico_{nome_limpo}.json")
                    
                    indice_musica = (indice_musica + 1) % len(audio_files)
                    manager.load_audio(indice_musica)
                    manager.play(indice_musica)
                    if pausado:
                        pygame.mixer.music.pause()
                        
            elif event.key == pygame.K_LEFT:
                if len(audio_files) > 0:
                    nome_limpo = audio_files[indice_musica].split('/')[-1].split('\\')[-1].replace('.wav', '')
                    repo.salvar(f"historico_{nome_limpo}.json")
                    
                    indice_musica = (indice_musica - 1) % len(audio_files)
                    manager.load_audio(indice_musica)
                    manager.play(indice_musica)
                    if pausado:
                        pygame.mixer.music.pause()
            
    ritmo = manager.get_beat_multiplier()
    frequencias = manager.get_current_frequencies(num_bandas=NUM_BOLAS)
    
    screen.fill((0, 0, 0)) 
    
    if len(audio_files) > 0:
        nome_atual = audio_files[indice_musica].split('/')[-1].split('\\')[-1].replace('.wav', '')
        texto_surface = fonte.render(f"Música: {nome_atual}", True, (255, 255, 255))
        screen.blit(texto_surface, (80, 40))
    
    for b in lista_bolas:
        if not pausado:
            b.update(frequencias, ritmo)
        
        pygame.draw.line(screen, b._cor_hex, (int(b._position_x), 650), (int(b._position_x), int(b._position_y)), 2)
        b.draw(screen)
        
    if not pausado:
        objeto_areia.update(lista_bolas, 720)  
        repo.registrar_estado(lista_bolas)  
        
    objeto_areia.draw(screen) 
        
    pygame.display.flip()
    clock.tick(200)
    
pygame.quit()