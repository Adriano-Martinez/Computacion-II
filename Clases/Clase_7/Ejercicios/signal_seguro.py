import signal
import time
import os

# Variable global como bandera
interrumpido = False

def handler_sigint(signum, frame):
    global interrumpido
    interrumpido = True  # Señal recibida

# Asociar SIGINT con el handler
signal.signal(signal.SIGINT, handler_sigint)

print(f"PID: {os.getpid()} - Presioná Ctrl+C para probar")
try:
    while True:
        if interrumpido:
            print("🔔 Se recibió una señal. Finalizando con gracia...")
            break
        print("Trabajando...")
        time.sleep(1)
except KeyboardInterrupt:
    pass
