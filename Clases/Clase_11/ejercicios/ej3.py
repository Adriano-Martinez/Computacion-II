import os
import time

def main():
    print(f"[Padre | PID={os.getpid()}] Creando un proceso hijo...")

    pid = os.fork()
    if pid == 0:
        # --- Proceso hijo ---
        print(f"[Hijo | PID={os.getpid()} | PPID={os.getppid()}] Iniciando trabajo...")
        for i in range(15):
            print(f"[Hijo | PID={os.getpid()} | PPID={os.getppid()}] Sigo vivo... ({i+1})")
            time.sleep(1)
        print(f"[Hijo | PID={os.getpid()}] Finalicé.")
    else:
        # --- Proceso padre ---
        print(f"[Padre | PID={os.getpid()}] Finalizo inmediatamente, dejando al hijo vivo.")
        os._exit(0)  # Padre termina y deja al hijo huérfano

if __name__ == "__main__":
    main()
