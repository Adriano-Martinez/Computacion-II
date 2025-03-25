import os
import time

pid = os.fork()

if pid == 0:  # Código del hijo
    time.sleep(5)  # Espera para que el padre termine primero
    print(f"Soy un proceso huérfano con PID {os.getpid()} y mi padre es {os.getppid()}")
else:
    print(f"Soy el proceso padre con PID {os.getpid()}, terminando ahora")
