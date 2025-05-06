from multiprocessing import Process, Value
import time

def incrementar(valor):
    for _ in range(100):
        time.sleep(0.01)
        valor.value += 1

if __name__ == "__main__":
    numero = Value('i', 0)  # 'i' = entero
    p1 = Process(target=incrementar, args=(numero,))
    p2 = Process(target=incrementar, args=(numero,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"Valor final: {numero.value}")
