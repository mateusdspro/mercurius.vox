"""
Configurações centralizadas do Mercurius.Vox
"""

import os

# =============================================================================
# TECLA DE ATIVAÇÃO
# =============================================================================
# Tecla Option DIREITA (⌥) - mais confiável que Fn
ACTIVATION_KEY = "Key.alt_r"

# =============================================================================
# MODELO WHISPER
# =============================================================================
# Opções: "tiny", "base", "small", "medium", "large"
# tiny  (~39MB)  - mais rápido, menor precisão
# base  (~140MB) - bom equilíbrio velocidade/precisão
# small (~460MB) - melhor precisão, mais lento
WHISPER_MODEL = "base"

# =============================================================================
# CONFIGURAÇÕES DE ÁUDIO
# =============================================================================
SAMPLE_RATE = 16000  # Hz - requisito do Whisper
CHANNELS = 1  # Mono

# =============================================================================
# DIRETÓRIOS
# =============================================================================
TEMP_DIR = "/tmp/mercurius_vox"
CACHE_DIR = os.path.expanduser("~/.cache/mercurius_vox")

# =============================================================================
# FEEDBACK VISUAL
# =============================================================================
SHOW_LANGUAGE = True       # Mostrar idioma detectado
SHOW_DURATION = True       # Mostrar duração da gravação
SHOW_VISUAL_INDICATOR = True  # Mostrar ícone de microfone quando gravando

# =============================================================================
# DIGITAÇÃO INTELIGENTE
# =============================================================================
SMART_TYPING = True  # Detecta campo de texto automaticamente
                     # True = digita SE houver campo, copia SE NÃO houver
                     # False = sempre só copia

# =============================================================================
# NOTIFICAÇÕES
# =============================================================================
SHOW_PASTE_NOTIFICATION = True  # Mostrar notificação quando copiar
NOTIFICATION_SOUND = "Glass"    # Som: Glass, Ping, Pop, Purr, Funk
