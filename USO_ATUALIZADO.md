# 🎤 Mercurius.Vox - Guia de Uso Atualizado

## ✅ MELHORIAS IMPLEMENTADAS

### 🛡️ Estabilidade
- ✅ **Nunca fecha sozinho** - Tratamento robusto de erros
- ✅ **Auto-recuperação** - Se houver erro, reinicia automaticamente
- ✅ **Logs de erro** - Mostra o que aconteceu se fechar

### 🚪 Múltiplas formas de sair
- ✅ **ESC** - Sai e volta ao Terminal
- ✅ **CTRL + C** - Interrompe e volta ao Terminal
- ✅ **Fechar janela** - Encerra completamente

---

## 🚀 COMO USAR

### 1️⃣ Abrir o app:

```bash
cd ~/Desktop/mercurius.vox && ./venv/bin/python main.py
```

### 2️⃣ Usar:
- **Segure Option direita** (⌥) → Fale → Solte
- ✅ Texto colado automaticamente em qualquer app!

### 3️⃣ Sair (3 opções):
- **ESC** → Sai e fica no Terminal
- **CTRL + C** → Sai e fica no Terminal
- **Fechar janela** → Fecha tudo

---

## 💡 USAR TERMINAL PARA OUTRAS COISAS

### Opção 1 - Nova Janela/Aba (RECOMENDADO):
- **CMD + N** → Nova janela do Terminal
- **CMD + T** → Nova aba no Terminal
- Mercurius continua na primeira janela/aba

### Opção 2 - Rodar em Background:

```bash
cd ~/Desktop/mercurius.vox && nohup ./venv/bin/python main.py > /tmp/mercurius.log 2>&1 &
```

**Para parar depois:**
```bash
pkill -f "python.*main.py"
```

**Ver se está rodando:**
```bash
ps aux | grep main.py
```

---

## 🔧 SE O APP FECHAR SOZINHO

Agora o app **mostra o erro** antes de fechar. Causas comuns:

1. **Permissão de Acessibilidade expirou**
   - Solução: Desabilite e habilite o Terminal em: Ajustes → Privacidade → Acessibilidade

2. **Erro no microfone**
   - Solução: Verifique permissão de Microfone

3. **Erro de memória** (gravação muito longa)
   - Solução: Fale em frases mais curtas

**O app agora tenta se recuperar automaticamente!**

---

## 📋 RECURSOS

- ✅ Português e inglês apenas
- ✅ Funciona em TODOS os apps
- ✅ Nunca perde permissões
- ✅ Estável para uso 24/7
- ✅ Múltiplas formas de sair

---

## 🌐 GitHub

```
https://github.com/mateusdspro/mercurius.vox
```

**Data da atualização:** 29/12/2024

