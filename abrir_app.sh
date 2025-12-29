#!/bin/bash

# =============================================================================
# Launcher simplificado do Mercurius.Vox
# Abre o terminal com o app rodando
# =============================================================================

APP_DIR="$(cd "$(dirname "$0")" && pwd)"

# Abrir em nova janela do Terminal.app
osascript <<EOF
tell application "Terminal"
    activate
    do script "cd '$APP_DIR' && ./venv/bin/python main.py"
end tell
EOF


