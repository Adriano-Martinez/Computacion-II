from multiprocessing import Process, Lock, Value

def sumar(lock, contador):
    for _ in range(100000):
        with lock:
            contador.value += 1

if __name__ == "__main__":
    lock = Lock()
    contador = Value('i', 0)  # entero compartido
    p1 = Process(target=sumar, args=(lock, contador))
    p2 = Process(target=sumar, args=(lock, contador))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Contador:", contador.value)
