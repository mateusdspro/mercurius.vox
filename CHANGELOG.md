# 🎯 MERCURIUS.VOX - MUDANÇAS APLICADAS

## ✅ O QUE FOI MODIFICADO:

### 1. **config.py** - Configuração de Idiomas
- ✅ Adicionado `LANGUAGE = "pt"` (português como padrão)
- ✅ Adicionado `ALLOWED_LANGUAGES = ["pt", "en"]` (bloqueia outros idiomas)

### 2. **transcriber.py** - Foco em PT/EN
- ✅ Importa configurações de idioma
- ✅ Força transcrição em português como base
- ✅ Bloqueia detecção de búlgaro, romeno, etc.
- ✅ Se detectar outro idioma, força português

### 3. **smart_typer.py** - Universalidade Total
- ✅ Funciona em TODOS os aplicativos (não mais lista específica)
- ✅ SEMPRE tenta colar automaticamente (CMD+V)
- ✅ Se não houver campo de texto, fica no clipboard

---

## 🎯 RESULTADO:

✅ **ChatGPT, Discord, Figma, qualquer app** → Funciona!
✅ **Apenas português e inglês** → Sem búlgaro/romeno
✅ **Sempre cola automaticamente** → CMD+V automático
✅ **Se não colar** → Fica no clipboard para colar manual

---

## 🚀 COMO TESTAR:

1. Feche o app atual (se estiver rodando)
2. Execute: `cd ~/Desktop/mercurius.vox && ./venv/bin/python main.py`
3. Segure Option direita (⌥) → Fale → Solte
4. Teste em: ChatGPT, Chrome, qualquer app!

---

## 📝 Data: 29/12/2024

