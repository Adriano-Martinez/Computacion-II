import os
import signal
import time

# Handler para SIGUSR1
def recibir_usr1(signum, frame):
    print(f"📡 Señal SIGUSR1 recibida por proceso {os.getpid()}")

# Registrar handler
signal.signal(signal.SIGUSR1, recibir_usr1)

print(f"PID actual: {os.getpid()}")
print("Esperando SIGUSR1...")

# Esperar
while True:
    time.sleep(1)
