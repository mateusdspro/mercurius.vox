"""
Módulo de transcrição usando Whisper local
"""

import whisper
import torch

from config import WHISPER_MODEL


class Transcriber:
    """Transcritor de áudio usando OpenAI Whisper local"""
    
    def __init__(self):
        self.model = None
        self.model_name = WHISPER_MODEL
        self.device = self._get_device()
    
    def _get_device(self) -> str:
        """Detecta o melhor dispositivo disponível (GPU/CPU)"""
        if torch.cuda.is_available():
            return "cuda"
        elif torch.backends.mps.is_available():
            # Apple Silicon (M1/M2/M3)
            return "mps"
        return "cpu"
    
    def load_model(self, callback=None):
        """
        Carrega o modelo Whisper
        
        Args:
            callback: Função opcional para feedback de progresso
        """
        if callback:
            callback(f"Carregando modelo Whisper '{self.model_name}' no {self.device}...")
        
        self.model = whisper.load_model(self.model_name, device=self.device)
        
        if callback:
            callback(f"Modelo carregado com sucesso!")
    
    def transcribe(self, audio_path: str) -> dict:
        """
        Transcreve um arquivo de áudio
        
        Args:
            audio_path: Caminho para o arquivo WAV
            
        Returns:
            dict: {
                "text": str,      # Texto transcrito
                "language": str,  # Idioma detectado
                "success": bool   # Se a transcrição foi bem sucedida
            }
        """
        if self.model is None:
            self.load_model()
        
        try:
            # Transcrever com detecção automática de idioma
            result = self.model.transcribe(
                audio_path,
                language=None,  # Detecta automaticamente
                task="transcribe",
                fp16=False  # Mais compatível com diferentes hardwares
            )
            
            text = result.get("text", "").strip()
            language = result.get("language", "unknown")
            
            # Mapear códigos de idioma para nomes
            language_names = {
                "pt": "Português",
                "en": "English",
                "es": "Español",
                "fr": "Français",
                "de": "Deutsch",
            }
            language_display = language_names.get(language, language)
            
            return {
                "text": text,
                "language": language_display,
                "language_code": language,
                "success": True
            }
            
        except Exception as e:
            return {
                "text": "",
                "language": "unknown",
                "language_code": "",
                "success": False,
                "error": str(e)
            }

