import argparse
import os
import time
import random
import multiprocessing
import subprocess

def tarea_hijo(id_hijo, verbose):
    """Simula trabajo en un proceso hijo"""
    duracion = random.randint(1, 5)
    if verbose:
        print(f"[Hijo {id_hijo} | PID={os.getpid()}] Trabajando durante {duracion} segundos...")
    time.sleep(duracion)
    if verbose:
        print(f"[Hijo {id_hijo} | PID={os.getpid()}] Finalizó.")

def main():
    # --- Manejo de argumentos con argparse ---
    parser = argparse.ArgumentParser(description="Gestor de procesos concurrentes")
    parser.add_argument("--num", type=int, required=True, help="Cantidad de procesos hijos a crear")
    parser.add_argument("--verbose", action="store_true", help="Activa mensajes detallados")
    args = parser.parse_args()

    print(f"[Padre | PID={os.getpid()}] Creando {args.num} procesos hijos...")

    # --- Crear procesos hijos ---
    procesos = []
    for i in range(args.num):
        p = multiprocessing.Process(target=tarea_hijo, args=(i, args.verbose))
        procesos.append(p)
        p.start()

    # --- Mostrar jerarquía de procesos con pstree ---
    print("\nJerarquía de procesos (pstree):")
    subprocess.run(["pstree", "-p", str(os.getpid())])

    # --- Esperar a que terminen los hijos ---
    for p in procesos:
        p.join()

    print(f"[Padre | PID={os.getpid()}] Todos los hijos terminaron.")

if __name__ == "__main__":
    main()
