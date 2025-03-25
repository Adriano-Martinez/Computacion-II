import os
import time

pid = os.fork()

if pid == 0:  # Código del hijo
    print(f"Soy el proceso hijo con PID {os.getpid()} (voy a terminar)")
else:  # Código del padre
    print(f"Soy el proceso padre con PID {os.getpid()}, mi hijo es {pid}")
    time.sleep(10)  # El padre sigue vivo, pero no llama a wait()

    # Usa "ps aux | grep Z" en otra terminal para ver el zombi
