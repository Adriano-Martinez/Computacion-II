import os

fifo_path = 'canal_fifo'

print("Lector esperando para abrir el FIFO...")
with open(fifo_path, 'r') as fifo:
    while True:
        linea = fifo.readline()
        if not linea:
            break  # Fin del stream
        print(f"Leído: {linea.strip()}")
