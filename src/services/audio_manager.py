import numpy as np
import librosa
from glob import glob
import pygame

pygame.mixer.init

audio_files = glob('../../assets/audios/*.wav')

class AudioManager:
    def __init__(self, audio_files):
        pygame.mixer.init()
        self._audio = audio_files
        self._current_data = None  #pressao sonora em cada milionesimo que varia de -1 a 1, o grafico disso aqui daria o desenho da onda e baiscamente um sinal
        self._sampler_rate = None  #amostras em um segundo de audio
        
    def load_audio(self, indice):
        caminho = self._audio[indice]
        data, rate = librosa.load(caminho)
        self._current_data = data
        self._sampler_rate = rate
    
    def play(self, indice):
        caminho = self._audio[indice]
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play()
        
    def get_current_amplitude(self):
        tempo_ms = pygame.mixer.music.get_pos()
        tempo_seg = tempo_ms / 1000.0
        
        indice = int(tempo_seg * self._sampler_rate)
        
        if self._current_data is not None and indice < len(self._current_data):
            return self._current_data[indice]
        
        return 0
