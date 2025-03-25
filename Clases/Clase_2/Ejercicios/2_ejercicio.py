import os
import time

pid = os.fork()

if pid == 0:  # Código del hijo
    time.sleep(3)  # Espera para que el padre termine primero
    print(f"Soy un proceso huérfano con PID {os.getpid()} y mi nuevo padre es {os.getppid()}")
else:
    print(f"Soy el proceso padre con PID {os.getpid()}, terminando ahora")
    os._exit(0)  # El padre finaliza antes que el hijo
