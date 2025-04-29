import signal
import os
import time

print(f"PID: {os.getpid()}")

# Ignorar Ctrl+C
signal.signal(signal.SIGINT, signal.SIG_IGN)
print("SIGINT ahora será ignorado. Presioná Ctrl+C para probar.")
time.sleep(5)

# Restaurar comportamiento por defecto
signal.signal(signal.SIGINT, signal.SIG_DFL)
print("SIGINT restaurado. Presioná Ctrl+C para detener el programa.")
while True:
    time.sleep(1)
