from multiprocessing import Process, Queue
import time

def productor(q):
    for i in range(5):
        print(f"[Productor] Enviando: {i}")
        q.put(i)
        time.sleep(1)

def consumidor(q):
    for _ in range(5):
        dato = q.get()
        print(f"[Consumidor] Recibido: {dato}")
        time.sleep(2)

if __name__ == "__main__":
    queue = Queue()

    p1 = Process(target=productor, args=(queue,))
    p2 = Process(target=consumidor, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("✅ Comunicación finalizada")
