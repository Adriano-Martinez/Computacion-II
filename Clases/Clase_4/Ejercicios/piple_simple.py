import os

def main():
    # 1. Crear el pipe
    r_fd, w_fd = os.pipe()

    # 2. Crear el proceso hijo
    pid = os.fork()

    if pid == 0:
        # --- Proceso Hijo ---
        os.close(w_fd)  # Cerramos extremo de escritura

        print("[Hijo] Esperando mensaje del padre...")
        mensaje = os.read(r_fd, 1024)  # Leer del pipe
        print(f"[Hijo] Recibido: {mensaje.decode()}")

        os.close(r_fd)

    else:
        # --- Proceso Padre ---
        os.close(r_fd)  # Cerramos extremo de lectura

        mensaje = "Hola desde el padre!"
        os.write(w_fd, mensaje.encode())  # Escribimos en el pipe
        print("[Padre] Mensaje enviado.")

        os.close(w_fd)

if __name__ == "__main__":
    main()
