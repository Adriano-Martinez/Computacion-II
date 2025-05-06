from multiprocessing import Process
import time

def say_hello():
    print("Hola desde el nuevo proceso")
    time.sleep(2)
    print("Proceso finalizado")

if __name__ == '__main__':
    p = Process(target=say_hello)
    p.start()         # Inicia el proceso
    p.join()          # Espera a que termine
    print("Proceso principal ha terminado")
