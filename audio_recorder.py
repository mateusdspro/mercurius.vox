"""
Módulo de gravação de áudio usando sounddevice
"""

import os
import uuid
import threading
import numpy as np
import sounddevice as sd
import soundfile as sf

from config import SAMPLE_RATE, CHANNELS, TEMP_DIR


class AudioRecorder:
    """Gravador de áudio com controle via threading"""
    
    def __init__(self):
        self.sample_rate = SAMPLE_RATE
        self.channels = CHANNELS
        self.recording = False
        self.audio_data = []
        self._lock = threading.Lock()
        
        # Criar diretório temporário se não existir
        os.makedirs(TEMP_DIR, exist_ok=True)
    
    def _audio_callback(self, indata, frames, time, status):
        """Callback chamado pelo sounddevice durante gravação"""
        if status:
            print(f"⚠️  Status: {status}")
        
        if self.recording:
            with self._lock:
                self.audio_data.append(indata.copy())
    
    def start(self):
        """Inicia a gravação de áudio"""
        with self._lock:
            self.audio_data = []
        self.recording = True
        
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            callback=self._audio_callback,
            dtype=np.float32
        )
        self.stream.start()
    
    def stop(self) -> str:
        """
        Para a gravação e salva o áudio em arquivo temporário
        
        Returns:
            str: Caminho do arquivo WAV salvo
        """
        self.recording = False
        self.stream.stop()
        self.stream.close()
        
        with self._lock:
            if not self.audio_data:
                return None
            
            # Concatenar todos os chunks de áudio
            audio = np.concatenate(self.audio_data, axis=0)
        
        # Gerar nome único para arquivo temporário
        filename = f"{uuid.uuid4().hex}.wav"
        filepath = os.path.join(TEMP_DIR, filename)
        
        # Salvar como WAV
        sf.write(filepath, audio, self.sample_rate)
        
        return filepath
    
    def get_duration(self) -> float:
        """Retorna a duração atual da gravação em segundos"""
        with self._lock:
            if not self.audio_data:
                return 0.0
            total_samples = sum(chunk.shape[0] for chunk in self.audio_data)
            return total_samples / self.sample_rate


def cleanup_temp_file(filepath: str):
    """Remove arquivo temporário após uso"""
    try:
        if filepath and os.path.exists(filepath):
            os.remove(filepath)
    except OSError:
        pass  # Ignora erros de remoção

