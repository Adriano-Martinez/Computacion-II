import os
import time

fifo_path = 'canal_fifo'

print("Escritor abriendo FIFO...")
with open(fifo_path, 'w') as fifo:
    for i in range(6):
        mensaje = f"Mensaje {i}\n"
        print(f"Enviando: {mensaje.strip()}")
        fifo.write(mensaje)
        fifo.flush()
        time.sleep(1)

