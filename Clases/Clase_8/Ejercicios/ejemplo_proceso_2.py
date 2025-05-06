from multiprocessing import Process
import os

def saludo():
    print(f"Hola desde el proceso hijo. PID: {os.getpid()}")

if __name__ == "__main__":
    print(f"PID del proceso principal: {os.getpid()}")

    p = Process(target=saludo)
    p.start()
    p.join()

    print("El proceso hijo ha terminado.")
