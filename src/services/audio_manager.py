import numpy as np
import librosa
from glob import glob

audio_files = glob('../../assets/audios/*.wav')

class AudioManager:
    def __init__(self,audio_files):
        self._audio = audio_files
        self._current_data = None
        self._sampler_rate = None
        
        
    
    def load_audio(self, indice):
        caminho = self._audio[indice]
        data, rate = librosa.load(caminho)
        self._current_data = data
        self._sampler_rate = rate
    
    def play(self._current_data):
        pygame.mixer.load()