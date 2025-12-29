#!/usr/bin/env python3
"""
Launcher do Mercurius.Vox com ícone na barra de menu
"""

import os
import sys
import threading
import subprocess
from pathlib import Path

# Adicionar diretório do script ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import rumps
    from main import MercuriusVox
except ImportError as e:
    # Fallback para execução direta
    print(f"⚠️  Importação falhou: {e}")
    print("🔄 Executando modo direto...")
    from main import MercuriusVox
    app = MercuriusVox()
    app.run()
    sys.exit(0)


class MercuriusVoxMenuBar(rumps.App):
    """App com ícone na barra de menu"""
    
    def __init__(self):
        super().__init__(
            name="Mercurius.Vox",
            icon=None,
            quit_button=None
        )
        
        # Menu items
        self.menu = [
            "🎤 Status: Aguardando...",
            None,  # Separador
            "📝 Ver Logs",
            None,
            "ℹ️ Sobre",
            rumps.MenuItem("🚪 Sair", callback=self.quit_app)
        ]
        
        # Título do ícone
        self.title = "🎙️"
        
        # Variável de controle
        self.vox_app = None
        self.vox_thread = None
        
    @rumps.clicked("📝 Ver Logs")
    def show_logs(self, _):
        """Mostra console com logs"""
        # Abrir Console.app filtrado
        subprocess.Popen([
            'open', '-a', 'Console.app'
        ])
        
    @rumps.clicked("ℹ️ Sobre")
    def show_about(self, _):
        """Mostra informações sobre o app"""
        rumps.alert(
            title="Mercurius.Vox v2.0",
            message=(
                "Transcrição de voz local com IA\n\n"
                "🎤 Aperte [Fn] para gravar\n"
                "💬 Solte para transcrever\n"
                "✍️ Digita automaticamente\n\n"
                "100% local, sem APIs externas"
            ),
            ok="Entendi"
        )
    
    def quit_app(self, _):
        """Sai do aplicativo"""
        rumps.quit_application()
    
    def start_vox(self):
        """Inicia o Mercurius.Vox em thread separada"""
        def run_vox():
            try:
                self.vox_app = MercuriusVox()
                self.vox_app.run()
            except Exception as e:
                print(f"❌ Erro no Mercurius.Vox: {e}")
        
        self.vox_thread = threading.Thread(target=run_vox, daemon=True)
        self.vox_thread.start()


def main():
    """Ponto de entrada"""
    try:
        app = MercuriusVoxMenuBar()
        app.start_vox()
        app.run()
    except Exception as e:
        print(f"❌ Erro ao iniciar menubar: {e}")
        print("🔄 Iniciando modo fallback...")
        vox = MercuriusVox()
        vox.run()


if __name__ == "__main__":
    main()


