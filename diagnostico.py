#!/usr/bin/env python3
"""
Teste de diagnóstico do Mercurius.Vox
"""

import sys
import time

print("\n" + "="*50)
print("🔍 DIAGNÓSTICO DO MERCURIUS.VOX")
print("="*50 + "\n")

# Teste 1: Imports
print("1️⃣ Testando imports...")
try:
    from pynput import keyboard
    print("   ✅ pynput OK")
except Exception as e:
    print(f"   ❌ pynput: {e}")
    sys.exit(1)

try:
    import sounddevice as sd
    print("   ✅ sounddevice OK")
except Exception as e:
    print(f"   ❌ sounddevice: {e}")
    sys.exit(1)

try:
    import whisper
    print("   ✅ whisper OK")
except Exception as e:
    print(f"   ❌ whisper: {e}")
    sys.exit(1)

# Teste 2: Microfone
print("\n2️⃣ Testando microfone...")
try:
    devices = sd.query_devices()
    input_device = sd.default.device[0]
    print(f"   ✅ Microfone padrão: {devices[input_device]['name']}")
    
    # Testar gravação rápida
    print("   🎤 Gravando 1 segundo de teste...")
    recording = sd.rec(16000, samplerate=16000, channels=1)
    sd.wait()
    
    import numpy as np
    level = np.abs(recording).max()
    
    if level > 0.001:
        print(f"   ✅ Microfone captando áudio! (nível: {level:.4f})")
    else:
        print(f"   ⚠️  Áudio muito baixo ou sem permissão (nível: {level:.4f})")
        
except Exception as e:
    print(f"   ❌ Erro no microfone: {e}")

# Teste 3: Detecção de teclas
print("\n3️⃣ Testando detecção de teclas...")
print("   Aperte QUALQUER TECLA nos próximos 5 segundos...")
print("   (Pode ser espaço, letra, etc.)")

detected = []

def on_press(key):
    detected.append(str(key))
    return False  # Para após primeira tecla

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join(timeout=5)

if detected:
    print(f"   ✅ Tecla detectada: {detected[0]}")
    print("   ✅ Monitoramento de teclado funcionando!")
else:
    print("   ❌ NENHUMA TECLA DETECTADA!")
    print("   🔴 PROBLEMA: Sem permissão de Acessibilidade!")
    print("\n   SOLUÇÃO:")
    print("   1. Ajustes → Privacidade → Acessibilidade")
    print("   2. Adiciona Terminal e ativa ✅")
    print("   3. FECHA e ABRE o Terminal de novo")

# Teste 4: Tecla Fn específica
print("\n4️⃣ Testando tecla Fn (F13)...")
print("   Aperte a tecla Fn nos próximos 5 segundos...")

fn_detected = []

def on_press_fn(key):
    if key == keyboard.Key.f13:
        fn_detected.append(True)
        print(f"   ✅ TECLA Fn DETECTADA!")
        return False
    return True

listener2 = keyboard.Listener(on_press=on_press_fn)
listener2.start()
listener2.join(timeout=5)

if not fn_detected:
    print("   ⚠️  Tecla Fn NÃO detectada")
    print("   Isso é normal! A tecla Fn pode não funcionar como esperado.")
    print("\n   💡 RECOMENDAÇÃO: Trocar para Option direita")

# Resumo
print("\n" + "="*50)
print("📊 RESUMO DO DIAGNÓSTICO")
print("="*50)

if detected:
    print("\n✅ TECLADO: Funcionando")
else:
    print("\n❌ TECLADO: SEM PERMISSÃO DE ACESSIBILIDADE")
    
print("\n📋 PRÓXIMOS PASSOS:")
if not detected:
    print("1. Dar permissão de Acessibilidade ao Terminal")
    print("2. Reiniciar o Terminal")
    print("3. Testar novamente")
else:
    print("1. Considerar trocar tecla Fn para Option direita")
    print("2. Ou empacotar como .app para permissões permanentes")

print("\n")


