from multiprocessing import Process, Queue
import time

def productor(q):
    for i in range(10):
        print(f"[Productor] Enviando: {i}")
        q.put(i)
        time.sleep(0.5)
    q.put(None)  # Señal de fin
    q.put(None)  # Otra señal de fin para el segundo consumidor

def consumidor(nombre, q):
    while True:
        dato = q.get()
        if dato is None:
            print(f"[{nombre}] Fin de datos")
            break
        print(f"[{nombre}] Recibido: {dato}")
        time.sleep(1)

if __name__ == "__main__":
    queue = Queue()

    p1 = Process(target=productor, args=(queue,))
    c1 = Process(target=consumidor, args=("Consumidor 1", queue))
    c2 = Process(target=consumidor, args=("Consumidor 2", queue))

    p1.start()
    c1.start()
    c2.start()

    p1.join()
    c1.join()
    c2.join()

    print("✅ Comunicación con múltiples consumidores finalizada.")
