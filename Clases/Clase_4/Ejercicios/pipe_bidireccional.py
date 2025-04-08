import os
import time

def main():
    # Crear dos pipes:
    # pipe1: padre escribe → hijo lee
    # pipe2: hijo escribe → padre lee
    pipe1_lectura, pipe1_escritura = os.pipe()
    pipe2_lectura, pipe2_escritura = os.pipe()

    pid = os.fork()

    if pid == 0:
        # ---------------------------
        # Proceso hijo
        # ---------------------------

        # Cierra extremos no usados
        os.close(pipe1_escritura)  # No escribe en pipe1
        os.close(pipe2_lectura)    # No lee de pipe2

        # Lee mensaje del padre
        mensaje_padre = os.read(pipe1_lectura, 1024).decode()
        print(f"[Hijo] Recibido del padre: {mensaje_padre}")

        # Enviar respuesta
        respuesta = "Hola padre, soy el hijo."
        os.write(pipe2_escritura, respuesta.encode())
        print("[Hijo] Respuesta enviada.")

        # Cierra extremos usados
        os.close(pipe1_lectura)
        os.close(pipe2_escritura)

    else:
        # ---------------------------
        # Proceso padre
        # ---------------------------

        # Cierra extremos no usados
        os.close(pipe1_lectura)    # No lee de pipe1
        os.close(pipe2_escritura)  # No escribe en pipe2

        # Espera pequeña para asegurar que el hijo esté listo
        time.sleep(0.1)

        # Enviar mensaje al hijo
        mensaje = "Hola hijo, soy tu padre."
        os.write(pipe1_escritura, mensaje.encode())
        print("[Padre] Mensaje enviado.")

        # Lee respuesta del hijo
        respuesta_hijo = os.read(pipe2_lectura, 1024).decode()
        print(f"[Padre] Respuesta recibida del hijo: {respuesta_hijo}")

        # Cierra extremos usados
        os.close(pipe1_escritura)
        os.close(pipe2_lectura)

if __name__ == "__main__":
    main()


