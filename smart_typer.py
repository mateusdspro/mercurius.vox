"""
Sistema inteligente de digitação/clipboard com notificações
Detecta se há campo de texto ativo e age de acordo
"""

import time
import subprocess
import pyperclip
from pynput.keyboard import Controller, Key
from AppKit import NSWorkspace

from config import SHOW_PASTE_NOTIFICATION, NOTIFICATION_SOUND


class SmartTyper:
    """Digita automaticamente OU copia para clipboard de forma inteligente"""
    
    def __init__(self):
        self.keyboard = Controller()
    
    def _show_paste_notification(self):
        """Mostra notificação nativa do macOS para colar"""
        if not SHOW_PASTE_NOTIFICATION:
            return
        
        try:
            notification_text = (
                f'display notification "Clique em um campo de texto e use ⌘ Cmd + V para colar" '
                f'with title "🎤 Mercurius.Vox" '
                f'sound name "{NOTIFICATION_SOUND}"'
            )
            
            subprocess.Popen([
                'osascript', '-e', notification_text
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass  # Ignora erros de notificação
    
    def has_active_text_field(self):
        """
        Verifica se há um campo de texto ativo
        
        Returns:
            bool: True se há campo de texto ativo, False caso contrário
        """
        try:
            workspace = NSWorkspace.sharedWorkspace()
            active_app = workspace.activeApplication()
            app_name = active_app.get('NSApplicationName', '')
            
            # Lista de apps conhecidos com campos de texto
            text_apps = [
                'Notes', 'TextEdit', 'Pages', 'Word', 'Microsoft Word',
                'Google Chrome', 'Chrome', 'Safari', 'Firefox',
                'Slack', 'WhatsApp', 'Telegram', 'Messages',
                'Mail', 'Notion', 'Bear', 'Obsidian',
                'Visual Studio Code', 'Cursor', 'Sublime Text',
                'Evernote', 'OneNote', 'Keynote', 'Numbers',
                'Terminal', 'iTerm', 'Atom', 'Code'
            ]
            
            # Verifica se é um app de texto
            for app in text_apps:
                if app.lower() in app_name.lower():
                    return True
            
            # Se não reconhecer, assume que NÃO tem campo
            return False
            
        except Exception:
            return False
    
    def process_text(self, text: str):
        """
        Processa o texto de forma inteligente:
        - Se há campo ativo → digita automaticamente
        - Se não há campo → copia + mostra notificação
        
        Args:
            text: Texto transcrito
            
        Returns:
            str: "typed" ou "copied"
        """
        if not text:
            return "error"
        
        # Sempre copia primeiro (backup)
        pyperclip.copy(text)
        
        # Verifica se deve digitar
        if self.has_active_text_field():
            # Há campo ativo - digita automaticamente
            time.sleep(0.15)
            
            self.keyboard.press(Key.cmd)
            self.keyboard.press('v')
            self.keyboard.release('v')
            self.keyboard.release(Key.cmd)
            
            return "typed"
        else:
            # Não há campo ativo - copia e mostra notificação
            self._show_paste_notification()
            return "copied"
    
    def force_type(self, text: str):
        """Força digitação (mesmo sem campo ativo)"""
        pyperclip.copy(text)
        time.sleep(0.1)
        
        self.keyboard.press(Key.cmd)
        self.keyboard.press('v')
        self.keyboard.release('v')
        self.keyboard.release(Key.cmd)
    
    def copy_only(self, text: str):
        """Só copia para clipboard e mostra notificação"""
        pyperclip.copy(text)
        self._show_paste_notification()



