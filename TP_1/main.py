import multiprocessing as mp
import time
import random
import datetime
import numpy as np
import json
import hashlib

# ---------- FUNCIONES AUXILIARES ----------

# Genera una muestra simulada con valores biométricos
def generar_muestra(contador):
    # Cada 10 muestras, fuerza una alerta
    if contador % 10 == 0:
        return {
            "timestamp": datetime.datetime.now().isoformat(),
            "frecuencia": random.randint(210, 220),  # alta frecuencia
            "presion": [random.randint(210, 220), random.randint(90, 110)],  # presión sistólica > 200
            "oxigeno": random.randint(85, 89)  # baja saturación
        }
    else:
        return {
            "timestamp": datetime.datetime.now().isoformat(),
            "frecuencia": random.randint(60, 180),
            "presion": [random.randint(110, 180), random.randint(70, 110)],
            "oxigeno": random.randint(90, 100)
        }


# ---------- ANALIZADOR DE SEÑALES ----------

# Recibe datos, mantiene una ventana móvil de 30 muestras, calcula media y desv.
def analizador(nombre, conn, queue_out):
    ventana = []

    try:
        while True:
            try:
                dato = conn.recv()
            except EOFError:
                break

            if dato == "FIN":
                break

            if nombre == "frecuencia":
                valor = dato["frecuencia"]
            elif nombre == "oxigeno":
                valor = dato["oxigeno"]
            elif nombre == "presion":
                valor = dato["presion"][0]  # sólo sistólica
            else:
                continue

            ventana.append(valor)
            if len(ventana) > 30:
                ventana.pop(0)

            media = float(np.mean(ventana))
            desv = float(np.std(ventana))

            resultado = {
                "tipo": nombre,
                "timestamp": dato["timestamp"],
                "media": media,
                "desv": desv
            }

            queue_out.put(resultado)
    except Exception as e:
        print(f"[{nombre}] Error: {e}")
    finally:
        conn.close()

# ---------- PROCESO VERIFICADOR ----------

# Espera resultados, detecta alertas, construye bloques y guarda la cadena en JSON
def verificador(queues, total_bloques=60, filename='blockchain.json'):
    blockchain = []
    prev_hash = "0" * 64

    try:
        for _ in range(total_bloques):
            resultados = {}
            while len(resultados) < 3:
                for q in queues:
                    if not q.empty():
                        res = q.get()
                        resultados[res["tipo"]] = res

            alerta = False
            if resultados["frecuencia"]["media"] >= 200:
                alerta = True
            if not (90 <= resultados["oxigeno"]["media"] <= 100):
                alerta = True
            if resultados["presion"]["media"] >= 200:
                alerta = True

            bloque = {
                "timestamp": resultados["frecuencia"]["timestamp"],
                "datos": {
                    "frecuencia": {
                        "media": resultados["frecuencia"]["media"],
                        "desv": resultados["frecuencia"]["desv"]
                    },
                    "presion": {
                        "media": resultados["presion"]["media"],
                        "desv": resultados["presion"]["desv"]
                    },
                    "oxigeno": {
                        "media": resultados["oxigeno"]["media"],
                        "desv": resultados["oxigeno"]["desv"]
                    }
                },
                "alerta": alerta,
                "prev_hash": prev_hash
            }

            hash_str = bloque["prev_hash"] + str(bloque["datos"]) + bloque["timestamp"]
            bloque["hash"] = hashlib.sha256(hash_str.encode()).hexdigest()

            blockchain.append(bloque)
            prev_hash = bloque["hash"]

            with open(filename, 'w') as f:
                json.dump(blockchain, f, indent=2)

            idx = len(blockchain) - 1
            print(f"[Verificador] Bloque {idx} | Hash: {bloque['hash']} | Alerta: {alerta}")

        print("[Verificador] Finalizado.")
    except Exception as e:
        print(f"[Verificador] Error: {e}")
    finally:
        for q in queues:
            q.close()

# ---------- PROCESO PRINCIPAL ----------

if __name__ == '__main__':
    mp.set_start_method("fork")  

    # Pipes para enviar datos
    parent_a, child_a = mp.Pipe()
    parent_b, child_b = mp.Pipe()
    parent_c, child_c = mp.Pipe()

    # Queues para recibir resultados
    queue_a = mp.Queue()
    queue_b = mp.Queue()
    queue_c = mp.Queue()

    # Crea procesos analizadores
    proc_a = mp.Process(target=analizador, args=("frecuencia", child_a, queue_a))
    proc_b = mp.Process(target=analizador, args=("presion", child_b, queue_b))
    proc_c = mp.Process(target=analizador, args=("oxigeno", child_c, queue_c))

    proc_a.start()
    proc_b.start()
    proc_c.start()

    # Crea y lanza proceso verificador
    queues = [queue_a, queue_b, queue_c]
    proc_verificador = mp.Process(target=verificador, args=(queues,))
    proc_verificador.start()

    # Genera y envia 60 muestras (1 por segundo)
    for i in range(60):
     muestra = generar_muestra(i)
     print(f"[Generador] {muestra}")
     parent_a.send(muestra)
     parent_b.send(muestra)
     parent_c.send(muestra)
     time.sleep(1)

    # Avisa fin a analizadores
    parent_a.send("FIN")
    parent_b.send("FIN")
    parent_c.send("FIN")

    # Cierra extremos de los pipes del padre
    parent_a.close()
    parent_b.close()
    parent_c.close()

    # Espera terminación de procesos
    proc_a.join()
    proc_b.join()
    proc_c.join()
    proc_verificador.join()

    print("[Main] Finalizado.")
