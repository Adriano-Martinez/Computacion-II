from multiprocessing import Process, Queue

def enviar(q):
    q.put("Hola desde el hijo")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=enviar, args=(q,))
    p.start()

    print(q.get())  # Recibe el mensaje desde la cola
    p.join()
