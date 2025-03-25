import os

for i in range(3):  # Crear 3 hijos
    pid = os.fork()
    
    if pid == 0:  # Código del hijo
        print(f"Soy el proceso hijo {i} con PID {os.getpid()}")
        os._exit(0)  # Termina el proceso hijo

# El padre espera a los hijos
for i in range(3):
    os.wait()
