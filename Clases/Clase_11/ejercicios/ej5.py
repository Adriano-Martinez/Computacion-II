import os

def main():
    print(f"[Padre | PID={os.getpid()}] Creando un pipe...")

    # Creamos un pipe: r -> lectura, w -> escritura
    r, w = os.pipe()

    pid = os.fork()
    if pid == 0:
        # --- Proceso hijo ---
        os.close(r)  # Cierra el extremo de lectura en el hijo
        mensaje = "Hola padre, soy tu hijo!".encode('utf-8')
        os.write(w, mensaje)
        os.close(w)  # Cierra el extremo de escritura
        print(f"[Hijo | PID={os.getpid()}] Mensaje enviado, termino.")
        os._exit(0)
    else:
        # --- Proceso padre ---
        os.close(w)  # Cierra el extremo de escritura en el padre
        mensaje_recibido = os.read(r, 1024)  # Leer hasta 1024 bytes
        os.close(r)  # Cierra el extremo de lectura
        print(f"[Padre | PID={os.getpid()}] Mensaje recibido: {mensaje_recibido.decode('utf-8')}")
        os.wait()  # Espera que el hijo termine

if __name__ == "__main__":
    main()
