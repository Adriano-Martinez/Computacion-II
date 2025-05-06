from multiprocessing import Process, Array

def llenar_array(arr):
    for i in range(len(arr)):
        arr[i] = i * 10

if __name__ == "__main__":
    datos = Array('i', 5)  # Array de 5 enteros
    p = Process(target=llenar_array, args=(datos,))
    p.start()
    p.join()

    print(list(datos))  # -> [0, 10, 20, 30, 40]
