import os
import time

fifo_path = "/tmp/mi_pipe_final"

# Crear FIFO si no existe
if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)

print("[Escritor] Esperando para escribir...")
with open(fifo_path, "w") as fifo:
    fifo.write("mensaje final desde escritor\n")
    print("[Escritor] Mensaje enviado.")
