import multiprocessing
import time
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "log.txt")

def escribir_log(lock, id_proceso):
    for i in range(3):  # Cada proceso escribe 3 mensajes
        tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f"Proceso {id_proceso} | Mensaje {i+1} | Hora: {tiempo}\n"
        
        # Usamos lock para evitar que dos procesos escriban a la vez
        with lock:
            with open(LOG_PATH, "a") as f:
                f.write(mensaje)
        
        # Espera para simular el trabajo
        time.sleep(0.5)

if __name__ == "__main__":
    # Se crea un Lock compartido
    lock = multiprocessing.Lock()

    # Lista de procesos
    procesos = []
    for i in range(5):  # 5 procesos
        p = multiprocessing.Process(target=escribir_log, args=(lock, i))
        procesos.append(p)
        p.start()

    # Esperamos a que terminen
    for p in procesos:
        p.join()

    print(f"Todos los procesos terminaron. Revisa {LOG_PATH} ✅")
