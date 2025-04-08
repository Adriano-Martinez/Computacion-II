import os

fifo_path = "/tmp/mi_pipe"

with open(fifo_path, "w") as fifo:
    fifo.write("Hola desde el escritor!\n")
    print("[Escritor] Mensaje enviado.")
