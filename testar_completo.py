#!/usr/bin/env python3
"""
Teste DEFINITIVO de permissões e tecla Fn
"""

import sys
import time

print("\n" + "="*60)
print("🔍 TESTE COMPLETO DO MERCURIUS.VOX")
print("="*60 + "\n")

# 1. Testar permissão de Acessibilidade
print("1️⃣ TESTANDO PERMISSÃO DE ACESSIBILIDADE...")
print("   ⏰ Aperte QUALQUER TECLA nos próximos 5 segundos...\n")

from pynput import keyboard

detected_keys = []

def on_press(key):
    detected_keys.append(str(key))
    print(f"   ✅ TECLA DETECTADA: {key}")
    return False  # Para após primeira tecla

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join(timeout=5)

if not detected_keys:
    print("\n   ❌ NENHUMA TECLA DETECTADA!")
    print("\n   🔴 PROBLEMA: SEM PERMISSÃO DE ACESSIBILIDADE!\n")
    print("   " + "="*56)
    print("   📋 SOLUÇÃO:")
    print("   " + "="*56)
    print("   1. Abra: Ajustes → Privacidade → Acessibilidade")
    print("   2. Clique no 🔒 cadeado e digite sua senha")
    print("   3. Procure 'Terminal' na lista")
    print("   4. Ative o ✅ checkbox ao lado de Terminal")
    print("   5. FECHE este Terminal completamente")
    print("   6. Abra um Terminal NOVO")
    print("   7. Execute este teste novamente")
    print("   " + "="*56 + "\n")
    sys.exit(1)

print(f"\n   ✅ PERMISSÃO OK! Tecla detectada: {detected_keys[0]}\n")

# 2. Testar tecla Fn específica
print("2️⃣ TESTANDO TECLA Fn...")
print("   ⏰ Aperte a tecla Fn nos próximos 5 segundos...\n")

fn_detected = []

def on_press_fn(key):
    key_str = str(key)
    print(f"   🔍 Tecla pressionada: {key_str}")
    
    if key == keyboard.Key.f13:
        fn_detected.append(True)
        print(f"   ✅ TECLA Fn DETECTADA COMO F13!")
        return False
    return True

listener2 = keyboard.Listener(on_press=on_press_fn)
listener2.start()
listener2.join(timeout=5)

print()

if fn_detected:
    print("   ✅ TECLA Fn FUNCIONA!\n")
    print("=" * 60)
    print("✅ TUDO CERTO! O APP VAI FUNCIONAR!")
    print("=" * 60)
    print("\n📋 PRÓXIMO PASSO:")
    print("   Execute: cd ~/Desktop/mercurius.vox && ./venv/bin/python main.py\n")
else:
    print("   ⚠️  TECLA Fn NÃO FOI DETECTADA COMO F13\n")
    print("   " + "="*56)
    print("   💡 SOLUÇÃO: TROCAR PARA TECLA Option DIREITA")
    print("   " + "="*56)
    print("\n   A tecla Fn do MacBook pode não funcionar como esperado.")
    print("   Vamos trocar para a tecla Option direita (⌥).\n")
    
    # Oferecer trocar automaticamente
    print("   Deseja trocar automaticamente? (s/n): ", end="")
    sys.stdout.flush()
    
    # Não esperar resposta, só mostrar a instrução
    print("\n\n   📝 PARA TROCAR MANUALMENTE:")
    print("   1. Abra: ~/Desktop/mercurius.vox/config.py")
    print("   2. Encontre a linha: ACTIVATION_KEY = \"Key.f13\"")
    print("   3. Troque para: ACTIVATION_KEY = \"Key.alt_r\"")
    print("   4. Salve o arquivo")
    print("   5. Execute o app novamente\n")

print()


