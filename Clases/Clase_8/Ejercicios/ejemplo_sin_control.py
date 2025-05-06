from multiprocessing import Process

contador = 0

def sumar():
    global contador
    for _ in range(100000):
        contador += 1

if __name__ == "__main__":
    p1 = Process(target=sumar)
    p2 = Process(target=sumar)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Contador:", contador)
