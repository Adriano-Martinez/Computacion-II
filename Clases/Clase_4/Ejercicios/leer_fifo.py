import os

fifo_path = "/tmp/mi_pipe"

with open(fifo_path, "r") as fifo:
    mensaje = fifo.read()
    print("[Lector] Mensaje recibido:", mensaje)
