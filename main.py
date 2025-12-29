#!/usr/bin/env python3
"""
Mercurius.Vox - Transcrição de voz local com Whisper

Uso: python main.py
Segure a tecla Fn para gravar, solte para transcrever.
"""

import sys
import time
import threading
from colorama import init, Fore, Style
from pynput import keyboard

from config import (
    ACTIVATION_KEY,
    SHOW_LANGUAGE,
    SHOW_DURATION,
    SHOW_VISUAL_INDICATOR,
    SMART_TYPING
)
from audio_recorder import AudioRecorder, cleanup_temp_file
from transcriber import Transcriber
from smart_typer import SmartTyper


# Inicializar colorama para cores no terminal
init()


class MercuriusVox:
    """Aplicação principal de transcrição de voz"""
    
    def __init__(self):
        self.recorder = AudioRecorder()
        self.transcriber = Transcriber()
        self.typer = SmartTyper()
        self.is_recording = False
        self.start_time = None
        
        # Parsear tecla de ativação
        self.activation_key = self._parse_key(ACTIVATION_KEY)
        
        # Indicador visual
        self.indicator = None
        if SHOW_VISUAL_INDICATOR:
            try:
                from visual_indicator import VisualIndicator
                self.indicator = VisualIndicator()
            except Exception as e:
                print(f"⚠️  Indicador visual não disponível: {e}")
                pass
    
    def _parse_key(self, key_str: str):
        """Converte string de tecla para objeto pynput"""
        key_map = {
            "Key.ctrl_r": keyboard.Key.ctrl_r,
            "Key.ctrl_l": keyboard.Key.ctrl_l,
            "Key.ctrl": keyboard.Key.ctrl,
            "Key.alt_r": keyboard.Key.alt_r,
            "Key.alt_l": keyboard.Key.alt_l,
            "Key.alt": keyboard.Key.alt,
            "Key.cmd": keyboard.Key.cmd,
            "Key.cmd_r": keyboard.Key.cmd_r,
            "Key.cmd_l": keyboard.Key.cmd_l,
            "Key.shift": keyboard.Key.shift,
            "Key.shift_r": keyboard.Key.shift_r,
            "Key.shift_l": keyboard.Key.shift_l,
            "Key.f13": keyboard.Key.f13,  # Tecla Fn
            "Key.f14": keyboard.Key.f14,
            "Key.f15": keyboard.Key.f15,
        }
        return key_map.get(key_str, keyboard.Key.f13)
    
    def _print_status(self, message: str, color=Fore.WHITE):
        """Imprime mensagem de status com cor"""
        print(f"{color}{message}{Style.RESET_ALL}")
    
    def _clear_line(self):
        """Limpa a linha atual do terminal"""
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()
    
    def on_press(self, key):
        """Callback quando tecla é pressionada"""
        if key == self.activation_key and not self.is_recording:
            self.is_recording = True
            self.start_time = time.time()
            self.recorder.start()
            
            # Mostrar indicador visual
            if self.indicator:
                self.indicator.show()
            
            self._print_status("🎤 Gravando... (solte a tecla para transcrever)", Fore.RED)
    
    def on_release(self, key):
        """Callback quando tecla é solta"""
        if key == self.activation_key and self.is_recording:
            self.is_recording = False
            duration = time.time() - self.start_time
            
            # Esconder indicador visual
            if self.indicator:
                self.indicator.hide()
            
            self._clear_line()
            self._print_status("⏳ Transcrevendo...", Fore.YELLOW)
            
            # Parar gravação e obter arquivo
            audio_path = self.recorder.stop()
            
            if audio_path is None:
                self._print_status("⚠️  Nenhum áudio capturado", Fore.YELLOW)
                return
            
            # Transcrever
            result = self.transcriber.transcribe(audio_path)
            
            # Limpar arquivo temporário
            cleanup_temp_file(audio_path)
            
            self._clear_line()
            
            if result["success"] and result["text"]:
                text = result["text"]
                
                # Processar texto de forma inteligente
                if SMART_TYPING:
                    action = self.typer.process_text(text)
                else:
                    self.typer.copy_only(text)
                    action = "copied"
                
                # Montar mensagem
                msg_parts = []
                
                if action == "typed":
                    msg_parts.append("✅ Digitado")
                elif action == "copied":
                    msg_parts.append("📋 Copiado (cole com CMD+V)")
                
                if SHOW_LANGUAGE:
                    msg_parts.append(f"[{result['language']}]")
                
                if SHOW_DURATION:
                    msg_parts.append(f"({duration:.1f}s)")
                
                msg_parts.append(f": {text}")
                
                self._print_status(" ".join(msg_parts), Fore.GREEN)
            else:
                error = result.get("error", "Erro desconhecido")
                self._print_status(f"❌ Falha na transcrição: {error}", Fore.RED)
            
            print()  # Nova linha para próxima gravação
        
        # ESC para sair
        if key == keyboard.Key.esc:
            self._print_status("\n👋 Saindo...", Fore.CYAN)
            return False
    
    def run(self):
        """Inicia o loop principal da aplicação"""
        # Banner
        print()
        print(f"{Fore.CYAN}╔══════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║      🎙️  Mercurius.Vox v2.0              ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║      Transcrição de voz local            ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚══════════════════════════════════════════╝{Style.RESET_ALL}")
        print()
        
        # Carregar modelo Whisper
        self.transcriber.load_model(callback=lambda msg: self._print_status(msg, Fore.YELLOW))
        print()
        
        # Instruções
        key_name = "Fn" if "f13" in ACTIVATION_KEY.lower() else ACTIVATION_KEY.replace("Key.", "").upper()
        self._print_status(f"📌 Segure [{key_name}] para gravar", Fore.CYAN)
        self._print_status(f"📌 Solte para transcrever", Fore.CYAN)
        
        if SMART_TYPING:
            self._print_status(f"📌 Digita automaticamente EM campos de texto", Fore.CYAN)
            self._print_status(f"📌 Copia para clipboard se NÃO houver campo", Fore.CYAN)
        else:
            self._print_status(f"📌 Sempre copia - cole com CMD+V", Fore.CYAN)
        
        self._print_status(f"📌 Pressione [ESC] para sair", Fore.CYAN)
        print()
        self._print_status("🔊 Pronto! Aguardando...", Fore.GREEN)
        print()
        
        # Iniciar listener de teclado
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()


def main():
    """Ponto de entrada principal"""
    try:
        app = MercuriusVox()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}👋 Interrompido pelo usuário{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Erro: {e}{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == "__main__":
    main()

