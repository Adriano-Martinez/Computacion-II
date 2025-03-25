import os

pid = os.fork()  # Crea un proceso hijo

if pid == 0:
    print(f"Soy el proceso hijo con PID {os.getpid()}")
else:
    print(f"Soy el proceso padre con PID {os.getpid()}, mi hijo es {pid}")
