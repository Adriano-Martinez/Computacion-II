import os

fifo_path = "/tmp/mi_pipe_final"

print("[Lector] Esperando mensaje...")
with open(fifo_path, "r") as fifo:
    mensaje = fifo.read()
    print("[Lector] Mensaje recibido:", mensaje)
