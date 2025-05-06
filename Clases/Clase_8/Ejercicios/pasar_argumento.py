from multiprocessing import Process
import os

def mostrar_mensaje(nombre):
    print(f"Hola, {nombre}. Soy el proceso con PID {os.getpid()}")

if __name__ == "__main__":
    print(f"PID del proceso principal: {os.getpid()}")

    # Crear proceso con argumento
    p = Process(target=mostrar_mensaje, args=("Estudiante",))
    p.start()
    p.join()

    print("Proceso con argumento finalizado.")
