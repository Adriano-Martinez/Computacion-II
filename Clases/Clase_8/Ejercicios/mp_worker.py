from multiprocessing import Process, Value, Lock
import time

def sumar(valor, lock):
    for _ in range(1000):
        time.sleep(0.001)  # Simula trabajo
        with lock:  # Sección crítica protegida
            valor.value += 1

if __name__ == "__main__":
    numero = Value('i', 0)     # Valor entero compartido
    lock = Lock()              # Lock para evitar condiciones de carrera

    p1 = Process(target=sumar, args=(numero, lock))
    p2 = Process(target=sumar, args=(numero, lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"Valor final esperado: 2000")
    print(f"Valor final real: {numero.value}")
