import os
import signal
import threading
import time

# Manejador de señal
def signal_handler(signum, frame):
    print(f"🔔 Señal recibida: {signum} en el hilo principal")

# Función que ejecutan los hilos secundarios
def hilo_secundario():
    print(f"🧵 Hilo secundario (PID: {os.getpid()}) iniciado.")
    time.sleep(10)
    print("🧵 Hilo secundario ha terminado.")

# Configurar el manejador de señales
signal.signal(signal.SIGUSR1, signal_handler)

# Crear hilos secundarios
hilos = []
for i in range(3):
    hilo = threading.Thread(target=hilo_secundario)
    hilos.append(hilo)
    hilo.start()

# Imprimir PID y esperar una señal
print(f"📌 Hilo principal (PID: {os.getpid()}) esperando señales...")
print(f"📌 Esperando en el hilo principal, presiona Ctrl+C o envía SIGUSR1 al proceso.")

# Esperar en el hilo principal
time.sleep(15)

# Enviar la señal SIGUSR1 al proceso
os.kill(os.getpid(), signal.SIGUSR1)

# Unir los hilos secundarios para que terminen
for hilo in hilos:
    hilo.join()

print("✅ Todos los hilos han terminado.")
