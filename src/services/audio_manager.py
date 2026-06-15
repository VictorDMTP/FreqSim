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
        self._sampler_rate = None  #amostras em um segundo de audio
        self._stft = None
        
    def load_audio(self, indice):
        caminho = self._audio[indice]
        data, rate = librosa.load(caminho)
        self._current_data = data
        self._sampler_rate = rate

        _, beats = librosa.beat.beat_track(y=data, sr=rate)
        self._beat_frames = beats
        
        self._stft = np.abs(librosa.stft(y=data, n_fft=2048, hop_length=512))
    
    def play(self, indice):
        caminho = self._audio[indice]
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play()
        
    
    
    def get_beat_multiplier(self):
        tempo_ms = pygame.mixer.music.get_pos()
        
        if tempo_ms < 1:
            return 1            
        frame_atual = librosa.time_to_frames(tempo_ms / 1000.0, sr = self._sampler_rate)

        if any(abs(frame_atual - beat) < 2 for beat in self._beat_frames):
            return 2.0
        return 1.0

    def get_current_frequencies(self, num_bandas=10):
        tempo_ms = pygame.mixer.music.get_pos()
        tempo_seg = tempo_ms / 1000.0
        
        frame_atual = librosa.time_to_frames(tempo_seg, sr=self._sampler_rate, hop_length=512)

        if self._stft is not None and frame_atual < self._stft.shape[1]:
            espectro_instante = self._stft[:, frame_atual]
            blocos = np.array_split(espectro_instante,num_bandas)
            return [float(np.mean(bloco)) * 3.0 for bloco in blocos]
        
        return [0.0] * num_bandas
    