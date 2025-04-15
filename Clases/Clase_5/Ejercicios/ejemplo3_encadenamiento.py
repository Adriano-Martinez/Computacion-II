from multiprocessing import Process, Queue
import time

def productor(q):
    for i in range(5):
        print(f"[Productor] Enviando: {i}")
        q.put(i)
        time.sleep(0.5)
    q.put(None)  # Fin

def transformador(q_in, q_out):
    while True:
        dato = q_in.get()
        if dato is None:
            q_out.put(None)
            break
        resultado = dato * dato
        print(f"[Transformador] {dato}^2 = {resultado}")
        q_out.put(resultado)
        time.sleep(0.5)

def consumidor(q):
    while True:
        dato = q.get()
        if dato is None:
            print("[Consumidor] Fin del procesamiento")
            break
        print(f"[Consumidor] Recibido: {dato}")
        time.sleep(0.5)

if __name__ == "__main__":
    q1 = Queue()
    q2 = Queue()

    p1 = Process(target=productor, args=(q1,))
    p2 = Process(target=transformador, args=(q1, q2))
    p3 = Process(target=consumidor, args=(q2,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("✅ Pipeline finalizado con éxito.")
