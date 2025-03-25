import os

pid = os.fork()

if pid == 0:  # Código del hijo
    os.execvp("ls", ["ls", "-l"])  # Reemplaza el proceso hijo con "ls -l"
else:
    os.wait()  # El padre espera a que termine el hijo
