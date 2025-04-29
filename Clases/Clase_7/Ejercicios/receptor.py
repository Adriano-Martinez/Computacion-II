import os
import signal
import time

def handler(signum, frame):
    print(f"🔔 Señal recibida: {signum} ({signal.Signals(signum).name})")

# Registrar el manejador
signal.signal(signal.SIGUSR1, handler)

print(f"📌 Esperando señales... Mi PID es {os.getpid()}")

# Esperar indefinidamente
while True:
    time.sleep(1)
