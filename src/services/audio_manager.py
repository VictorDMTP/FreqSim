import numpy as np
import librosa
import librosa.beat
from glob import glob
import pygame

pygame.mixer.init

audio_files = glob('../../assets/audios/*.wav')

class AudioManager:
    def __init__(self, audio_files):
        pygame.mixer.init()
        self._audio = audio_files
        self._beat_frames = []
        self._bpm = 0
        self._current_data = None  #pressao sonora em cada milionesimo que varia de -1 a 1, o grafico disso aqui daria o desenho da onda e baiscamente um sinal
        self._sampler_rate = None  #amostras em um segundo de audio
        
    def load_audio(self, indice):
        caminho = self._audio[indice]
        data, rate = librosa.load(caminho)
        self._current_data = data
        self._sampler_rate = rate

        tempo, beats = librosa.beat.beat_track(y=data, sr=rate)
        self._beat_frames = beats
        self._bpm = tempo
    
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
    
    def get_beat_multiplier(self):
        tempo_ms = pygame.mixer.music.get_pos()
        
        if tempo_ms < 1:
            return 1            
        frame_atual = librosa.time_to_frames(tempo_ms / 1000.0, sr = self._sampler_rate)

        if any(abs(frame_atual - beat) < 2 for beat in self._beat_frames):
            return 2.0
        return 1.0
