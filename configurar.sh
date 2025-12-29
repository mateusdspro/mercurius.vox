#!/bin/bash

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  🎤 MERCURIUS.VOX - CONFIGURAÇÃO AUTOMÁTICA               ║"
echo "╔════════════════════════════════════════════════════════════╗"
echo ""

# Verificar se tem permissão
echo "🔍 Verificando permissões..."
echo ""

# Tentar abrir Ajustes diretamente
echo "📱 Abrindo Ajustes de Privacidade para você..."
echo ""
open "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"

sleep 2

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  ⚠️  ATENÇÃO - FAÇA ISSO AGORA:                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "  Uma janela de Ajustes acabou de abrir!"
echo ""
echo "  1️⃣  Clique no 🔒 CADEADO (canto inferior esquerdo)"
echo "     Digite sua senha"
echo ""
echo "  2️⃣  Procure 'Terminal' na lista"
echo ""
echo "  3️⃣  ATIVE o ✅ ao lado de Terminal"
echo ""
echo "  4️⃣  Volte aqui e aperte ENTER quando terminar"
echo ""
echo "════════════════════════════════════════════════════════════"
echo ""
read -p "👆 Apertou ENTER quando der a permissão... " 

echo ""
echo "✅ Ótimo! Agora vou REINICIAR o Terminal para você..."
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  🔄 APÓS O TERMINAL REINICIAR:                             ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "  Execute este comando:"
echo ""
echo "  cd ~/Desktop/mercurius.vox && ./venv/bin/python main.py"
echo ""
echo "  Depois:"
echo ""
echo "  • Segure Option DIREITA (⌥) - canto inferior direito"
echo "  • Fale o que quiser"
echo "  • Solte a tecla"
echo "  • ✅ Texto transcrito!"
echo ""
echo "════════════════════════════════════════════════════════════"
echo ""
echo "🔄 Reiniciando Terminal em 3 segundos..."
sleep 3

# Fechar este terminal e abrir novo
osascript -e 'tell application "Terminal" to quit'
sleep 1
open -a Terminal


