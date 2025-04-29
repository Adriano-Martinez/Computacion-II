import os
import signal
import time

def enviar_senal(signum, frame):
    print("👨‍💻 Productor: señal enviada al consumidor")
    os.kill(padre_pid, signal.SIGUSR1)

if __name__ == '__main__':
    padre_pid = int(input("🔢 Ingresá el PID del consumidor: "))
    print(f"Productor PID: {os.getpid()}")
    
    signal.signal(signal.SIGALRM, enviar_senal)

    while True:
        print("⏳ Esperando para enviar nueva señal...")
        signal.alarm(5)  # Dispara SIGALRM en 5 segundos
        time.sleep(5)    # Espera que la señal se dispare
