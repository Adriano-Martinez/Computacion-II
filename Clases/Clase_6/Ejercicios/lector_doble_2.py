import os
import time

fifo_path = 'canal_fifo'

print("[Proceso 2] Abriendo FIFO para lectura...")
with open(fifo_path, 'r') as fifo:
    for i in range(3):
        mensaje = fifo.readline().strip()
        print(f"[Proceso 2] Leído: {mensaje}")
        time.sleep(1)
