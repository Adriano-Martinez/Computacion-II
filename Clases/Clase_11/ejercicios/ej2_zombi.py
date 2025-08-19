import os
import time

def main():
    print(f"[Padre | PID={os.getpid()}] Creando un proceso hijo...")

    pid = os.fork()  # Crear proceso hijo
    if pid == 0:
        # --- Proceso hijo ---
        print(f"[Hijo | PID={os.getpid()}] Finalizo inmediatamente.")
        os._exit(0)  # Termina sin esperar nada
    else:
        # --- Proceso padre ---
        print(f"[Padre | PID={os.getpid()}] Hijo creado con PID={pid}")
        print("[Padre] No recolectaré al hijo por 10 segundos...")
        time.sleep(10)

        # En este punto, durante los 10s el hijo está como zombi
        print("[Padre] Ahora recolecto al hijo con wait().")
        os.wait()  # Recolecta el estado del hijo
        print("[Padre] El proceso hijo ya no es zombi.")

if __name__ == "__main__":
    main()
