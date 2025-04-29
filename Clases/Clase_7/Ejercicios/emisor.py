import os
import signal
import time

# Reemplazá este número con el PID del receptor
pid_receptor = int(input("🔧 Ingresá el PID del receptor: "))

print(f"🚀 Enviando SIGUSR1 al proceso {pid_receptor}...")
os.kill(pid_receptor, signal.SIGUSR1)
