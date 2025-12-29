# 🎙️ Mercurius.Vox

Transcrição de voz local para macOS usando Whisper. Uma alternativa 100% offline a apps como Flow.

## ✨ Funcionalidades

- **Push-to-talk**: Segure uma tecla para gravar, solte para transcrever
- **100% offline**: Nenhum dado enviado para servidores externos
- **Detecção automática de idioma**: Português, Inglês e outros
- **Clipboard automático**: Texto copiado automaticamente para colar
- **Suporte GPU**: Usa Apple Silicon (MPS) ou CUDA quando disponível

## 📋 Requisitos

- macOS (testado em Sonoma)
- Python 3.9+
- Homebrew (para dependências de áudio)

## 🚀 Instalação

### 1. Instalar dependências do sistema

```bash
# Instalar portaudio (necessário para sounddevice)
brew install portaudio
```

### 2. Criar ambiente virtual (recomendado)

```bash
cd /path/to/Mercurius.Vox
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências Python

```bash
pip install -r requirements.txt
```

### 4. Dar permissões no macOS

O app precisa de duas permissões:

1. **Acessibilidade** (para detectar teclas):
   - Preferências do Sistema → Privacidade e Segurança → Acessibilidade
   - Adicione seu Terminal ou IDE (VS Code, Cursor, etc.)

2. **Microfone**:
   - Será solicitado automaticamente na primeira execução

## 🎮 Uso

```bash
python main.py
```

### Controles

| Ação | Tecla |
|------|-------|
| Gravar | Segure `CTRL direito` |
| Transcrever | Solte `CTRL direito` |
| Sair | `ESC` |

### Exemplo de uso

```
╔══════════════════════════════════════════╗
║      🎙️  Mercurius.Vox v1.0              ║
║      Transcrição de voz local            ║
╚══════════════════════════════════════════╝

Carregando modelo Whisper 'base' no mps...
Modelo carregado com sucesso!

📌 Segure [CTRL_R] para gravar
📌 Solte para transcrever e copiar
📌 Pressione [ESC] para sair

🔊 Pronto! Aguardando...

🎤 Gravando... (solte a tecla para transcrever)
✅ Copiado [Português] (2.3s): Olá, este é um teste de transcrição.
```

## ⚙️ Configuração

Edite `config.py` para personalizar:

```python
# Tecla de ativação
ACTIVATION_KEY = "Key.ctrl_r"  # Opções: Key.ctrl_l, Key.alt_r, Key.cmd, etc.

# Modelo Whisper
WHISPER_MODEL = "base"  # Opções: tiny, base, small, medium, large
```

### Modelos Whisper

| Modelo | Tamanho | Velocidade | Precisão |
|--------|---------|------------|----------|
| tiny | ~39MB | Muito rápido | Baixa |
| base | ~140MB | Rápido | Boa |
| small | ~460MB | Médio | Muito boa |
| medium | ~1.5GB | Lento | Alta |
| large | ~2.9GB | Muito lento | Máxima |

## 🔧 Solução de Problemas

### "Permission denied" ou teclas não detectadas

1. Vá em **Preferências do Sistema → Privacidade e Segurança → Acessibilidade**
2. Remova e adicione novamente seu Terminal/IDE
3. Reinicie o Terminal/IDE

### "No audio captured"

1. Verifique se o microfone está funcionando
2. Verifique permissões de microfone nas Preferências do Sistema
3. Teste com `python -c "import sounddevice; print(sounddevice.query_devices())"`

### Transcrição lenta

1. Use um modelo menor: `WHISPER_MODEL = "tiny"` ou `"base"`
2. Verifique se está usando GPU: o log deve mostrar `mps` (Apple Silicon) ou `cuda`

## 📁 Estrutura do Projeto

```
Mercurius.Vox/
├── main.py              # Ponto de entrada
├── audio_recorder.py    # Captura de áudio
├── transcriber.py       # Transcrição com Whisper
├── config.py            # Configurações
├── requirements.txt     # Dependências
└── README.md            # Este arquivo
```

## 📄 Licença

MIT License - Use como quiser!

