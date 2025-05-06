from multiprocessing import Pool

def cuadrado(x):
    return x * x

if __name__ == "__main__":
    pool = Pool(4)  # Creación de un pool con 4 procesos
    resultados = pool.map(cuadrado, [1, 2, 3, 4, 5])
    print(resultados)
    pool.close()  # Cierra el pool
    pool.join()   # Espera a que todos los procesos terminen
