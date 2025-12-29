# 🎤 Como Usar o Mercurius.Vox

## ✅ SOLUÇÃO DEFINITIVA PARA PERMISSÕES PERMANENTES

### 🚀 ABRIR O APLICATIVO

Você tem **3 opções** (todas fazem a mesma coisa):

1. **Clique duplo** em: `Abrir Mercurius.command` (no Desktop)
2. **Clique duplo** em: `MercuriusVox.app` (no Desktop)  
3. **No Terminal**, execute:
   ```bash
   cd ~/Desktop/mercurius.vox && ./venv/bin/python main.py
   ```

---

### 🔐 PERMISSÕES (APENAS NA PRIMEIRA VEZ)

Quando abrir pela **primeira vez**, o macOS vai pedir:

#### 1️⃣ Permissão de Microfone
- Pop-up: **"Terminal" gostaria de acessar o microfone**
- Clique em: **Permitir**

#### 2️⃣ Permissão de Acessibilidade
- Mensagem no terminal: `This process is not trusted!`
- Faça:
  1. Abra **Ajustes do Sistema** → **Privacidade e Segurança** → **Acessibilidade**
  2. Clique no **🔒 cadeado** (canto inferior esquerdo) e digite sua senha
  3. Procure **Terminal** na lista
  4. Ative o **✅ checkbox** ao lado de Terminal
  5. **FECHE** e **ABRA** o Terminal de novo

**✨ Pronto! As permissões agora são PERMANENTES (mesmo após reiniciar o Mac)!**

---

### 🎙️ COMO USAR

1. Veja a mensagem no terminal: `🔊 Pronto! Aguardando...`
2. **Segure** a tecla **Fn** (canto inferior esquerdo do teclado)
3. **Fale** o que você quer ditar
4. **Solte** a tecla Fn
5. Aguarde alguns segundos... ⏳
6. ✅ O texto será:
   - **Digitado automaticamente** se você estiver em um campo de texto
   - **Copiado** para o clipboard se não houver campo ativo
     - Nesse caso, aparece uma **notificação** dizendo para colar com `CMD+V`

---

### 🛑 PARAR O APLICATIVO

- Aperte **ESC** no terminal
- Ou feche a janela do terminal

---

### 🚀 INICIAR AUTOMATICAMENTE COM O MAC

1. Abra **Ajustes do Sistema**
2. Vá em **Geral** → **Iniciar ao Fazer Login**
3. Clique no **[+]**
4. Selecione `MercuriusVox.app` (no Desktop)
5. Pronto! O app vai abrir sozinho quando você ligar o Mac

---

### 🔧 PROBLEMAS?

#### ❌ "This process is not trusted!"
- **Causa:** Falta permissão de Acessibilidade
- **Solução:** Siga o passo 2️⃣ acima (Permissão de Acessibilidade)

#### ❌ "Nenhum áudio capturado"
- **Causa:** Falta permissão de Microfone
- **Solução:** 
  - Ajustes → Privacidade → Microfone → Terminal ✅
  - FECHE e ABRA o Terminal de novo

#### ❌ Permissões somem após reiniciar
- **Causa:** Está usando via Terminal comum
- **Solução:** Use o `MercuriusVox.app` em vez do Terminal
  - O `.app` mantém permissões permanentes!

---

### 💡 DICAS

- **Tecla Fn não funciona?** Edite `config.py` e troque para `Key.alt_r` (Option direita)
- **Quer sempre copiar?** Edite `config.py` e mude `SMART_TYPING = False`
- **Modelo muito lento?** Use `WHISPER_MODEL = "tiny"` (menos preciso, mais rápido)
- **Modelo muito impreciso?** Use `WHISPER_MODEL = "medium"` (mais preciso, mais lento)

---

## ✅ RESUMO RÁPIDO

```bash
# 1. Abrir
Clique duplo em: "Abrir Mercurius.command"

# 2. Dar permissões (só na primeira vez)
Microfone → Permitir
Acessibilidade → Terminal → ✅

# 3. Usar
Segure Fn → Fale → Solte → ✅ Texto digitado/copiado

# 4. Parar
Aperte ESC
```

---

**🎉 Pronto! Agora você tem um sistema de ditado por voz 100% local e gratuito!**


