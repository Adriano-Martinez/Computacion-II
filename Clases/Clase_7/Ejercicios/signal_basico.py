import signal
import time
import os

def handler_sigint(signum, frame):
    print(f"\n🔔 Señal recibida: {signum} (SIGINT)")
    print("El programa no se detendrá, pero ha sido interrumpido.")

# Asociar SIGINT (Ctrl+C) con el manejador personalizado
signal.signal(signal.SIGINT, handler_sigint)

print(f"PID del proceso: {os.getpid()}")
print("Presiona Ctrl+C para enviar SIGINT. Esperando...")

# Bucle infinito para mantener vivo el proceso
while True:
    time.sleep(1)
