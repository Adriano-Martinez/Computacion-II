import os
import sys
import time

def main():
    print(f"[Padre | PID={os.getpid()}] Creando un proceso hijo...")

    pid = os.fork()
    if pid == 0:
        # --- Proceso hijo ---
        print(f"[Hijo | PID={os.getpid()}] Reemplazando con 'ls -l' usando exec()...")
        # Reemplaza el proceso hijo con "ls -l"
        os.execlp("ls", "ls", "-l")
    else:
        # --- Proceso padre ---
        print(f"[Padre | PID={os.getpid()}] Esperando al hijo con PID={pid}...")
        os.wait()
        print("[Padre] El hijo terminó.")

if __name__ == "__main__":
    main()
