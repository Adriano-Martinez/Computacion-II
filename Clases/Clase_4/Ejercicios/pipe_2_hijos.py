import os

def hijo1(entrada, salida):
    os.dup2(entrada, 0)   # redirige stdin
    os.dup2(salida, 1)    # redirige stdout
    os.close(entrada)
    os.close(salida)
    os.execlp("tr", "tr", "a-z", "A-Z")

def hijo2(entrada, salida):
    os.dup2(entrada, 0)
    os.dup2(salida, 1)    # redirige stdout para que el padre lo lea
    os.close(entrada)
    os.close(salida)
    os.execlp("wc", "wc", "-w")

def main():
    r1, w1 = os.pipe()  # padre → hijo1
    r2, w2 = os.pipe()  # hijo1 → hijo2
    r3, w3 = os.pipe()  # hijo2 → padre (nuevo!)

    if os.fork() == 0:
        # Hijo1: transforma a mayúsculas
        os.close(w1)
        os.close(r2)
        os.close(r3)
        os.close(w3)
        hijo1(r1, w2)

    if os.fork() == 0:
        # Hijo2: cuenta palabras
        os.close(w2)
        os.close(w1)
        os.close(r1)
        os.close(r3)
        hijo2(r2, w3)

    # Padre
    os.close(r1)
    os.close(r2)
    os.close(w2)
    os.close(w3)

    mensaje = b"hola mundo desde pipes\n"
    os.write(w1, mensaje)
    os.close(w1)

    resultado = os.read(r3, 1024).decode()
    print(f"[Padre] Resultado final: {resultado.strip()}")
    os.close(r3)

if __name__ == "__main__":
    main()
