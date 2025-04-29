import signal
import os
import time

# Handler personalizado
def handler_usr1(signum, frame):
    print(f"🛰️  Señal recibida: {signum} ({signal.strsignal(signum)})")

# Mostrar PID
print(f"PID del proceso: {os.getpid()}")

# Registrar handler
signal.signal(signal.SIGUSR1, handler_usr1)

# Verificar el handler actual
actual = signal.getsignal(signal.SIGUSR1)
print(f"Handler registrado para SIGUSR1: {actual}")

# Esperar señal
print("Esperando señal SIGUSR1... Podés enviarla desde otra terminal con:")
print(f"kill -10 {os.getpid()}")

# Pausa
signal.pause()
