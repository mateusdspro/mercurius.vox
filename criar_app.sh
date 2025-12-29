#!/bin/bash

# =============================================================================
# Criador de .app do Mercurius.Vox (SEM SUDO)
# Cria aplicativo na pasta do usuário
# =============================================================================

echo "🚀 Criando MercuriusVox.app..."
echo ""

APP_NAME="MercuriusVox"
APP_DIR="$HOME/Desktop/${APP_NAME}.app"
CONTENTS_DIR="${APP_DIR}/Contents"
MACOS_DIR="${CONTENTS_DIR}/MacOS"
RESOURCES_DIR="${CONTENTS_DIR}/Resources"

# 1. Limpar app antigo
if [ -d "$APP_DIR" ]; then
    echo "🗑️  Removendo versão antiga..."
    rm -rf "$APP_DIR"
fi

# 2. Criar estrutura
echo "📁 Criando estrutura..."
mkdir -p "$MACOS_DIR"
mkdir -p "$RESOURCES_DIR"

# 3. Copiar código Python
echo "📦 Copiando código..."
cp -r ~/Desktop/mercurius.vox/* "$RESOURCES_DIR/"

# 4. Criar script de inicialização
echo "✍️  Criando launcher..."
cat > "$MACOS_DIR/MercuriusVox" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")/../Resources"
./venv/bin/python main.py
EOF

chmod +x "$MACOS_DIR/MercuriusVox"

# 5. Criar Info.plist
echo "⚙️  Configurando Info.plist..."
cat > "$CONTENTS_DIR/Info.plist" << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>MercuriusVox</string>
    <key>CFBundleDisplayName</key>
    <string>Mercurius.Vox</string>
    <key>CFBundleIdentifier</key>
    <string>com.mercurius.vox</string>
    <key>CFBundleVersion</key>
    <string>2.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleExecutable</key>
    <string>MercuriusVox</string>
    <key>NSMicrophoneUsageDescription</key>
    <string>Mercurius.Vox precisa acessar o microfone para transcrever sua voz.</string>
    <key>NSAppleEventsUsageDescription</key>
    <string>Mercurius.Vox precisa controlar o teclado para digitar o texto transcrito.</string>
    <key>LSUIElement</key>
    <true/>
</dict>
</plist>
EOF

# 6. Ajustar permissões
chmod -R 755 "$APP_DIR"

# 7. Resetar permissões antigas do Terminal
echo ""
echo "🔄 Resetando permissões antigas do Terminal..."
tccutil reset Microphone com.apple.Terminal 2>/dev/null
tccutil reset Accessibility com.apple.Terminal 2>/dev/null

echo ""
echo "✅ SUCESSO! Aplicativo criado:"
echo "   📍 $APP_DIR"
echo ""
echo "═════════════════════════════════════════════════════════"
echo "📋 COMO USAR (PERMISSÕES PERMANENTES):"
echo "═════════════════════════════════════════════════════════"
echo ""
echo "1️⃣  Abrir o aplicativo (clique duplo no Desktop):"
echo "   🖱️  Ou execute: open ~/Desktop/${APP_NAME}.app"
echo ""
echo "2️⃣  Dar permissões (APENAS UMA VEZ):"
echo "   • Ajustes → Privacidade → Microfone → MercuriusVox ✅"
echo "   • Ajustes → Privacidade → Acessibilidade → MercuriusVox ✅"
echo ""
echo "3️⃣  ✨ As permissões agora são PERMANENTES!"
echo "   (Funcionará mesmo após reiniciar o Mac)"
echo ""
echo "💡 INICIAR AUTOMATICAMENTE:"
echo "   1. Ajustes → Geral → Iniciar ao Fazer Login"
echo "   2. Clique no [+]"
echo "   3. Selecione MercuriusVox.app"
echo ""
echo "═════════════════════════════════════════════════════════"
echo ""
