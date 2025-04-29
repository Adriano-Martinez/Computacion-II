import os
import signal
import time

def recibir_datos(signum, frame):
    print("🔔 Consumidor: Recibí la señal de datos listos del productor.")

if __name__ == '__main__':
    signal.signal(signal.SIGUSR1, recibir_datos)  # Establece el handler para SIGUSR1
    print(f"Consumidor PID: {os.getpid()}")

    while True:
        time.sleep(5)
