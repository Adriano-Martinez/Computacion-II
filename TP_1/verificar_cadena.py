import json
import hashlib
import os

# Verifica la integridad de la blockchain, genera estadísticas y un reporte
def verificar_blockchain(filename='blockchain.json'):
    if not os.path.exists(filename):
        print(f"Archivo '{filename}' no encontrado.")
        return

    with open(filename, 'r') as f:
        blockchain = json.load(f)

    corruptos = []
    alertas = 0
    detalles_alertas = []
    total_bloques = len(blockchain)

    suma_frec = 0.0
    suma_pres = 0.0
    suma_oxi = 0.0

    for i, bloque in enumerate(blockchain):
        prev_hash = "0" * 64 if i == 0 else blockchain[i - 1]['hash']

        datos_str = str(bloque["datos"])
        timestamp = bloque["timestamp"]
        hash_calc = hashlib.sha256((prev_hash + datos_str + timestamp).encode()).hexdigest()

        if hash_calc != bloque["hash"]:
            corruptos.append(i)

        if bloque.get("alerta", False):
            alertas += 1

            # Verifico qué señales están en alerta
            alertas_bloque = []
            freq = bloque["datos"]["frecuencia"]["media"]
            pres = bloque["datos"]["presion"]["media"]
            oxi = bloque["datos"]["oxigeno"]["media"]

            if freq >= 200:
                alertas_bloque.append(f"Frecuencia cardíaca media: {freq} (≥ 200 bpm)")
            if pres >= 200:
                alertas_bloque.append(f"Presión sistólica media: {pres} (≥ 200 mmHg)")
            if oxi < 90 or oxi > 100:
                alertas_bloque.append(f"Saturación de oxígeno media: {oxi} (fuera de rango 90-100%)")

            detalles_alertas.append({
                "timestamp": timestamp,
                "alertas": alertas_bloque
            })

        suma_frec += bloque["datos"]["frecuencia"]["media"]
        suma_pres += bloque["datos"]["presion"]["media"]
        suma_oxi += bloque["datos"]["oxigeno"]["media"]

    promedio_frec = suma_frec / total_bloques if total_bloques > 0 else 0
    promedio_pres = suma_pres / total_bloques if total_bloques > 0 else 0
    promedio_oxi = suma_oxi / total_bloques if total_bloques > 0 else 0

    # Informa por consola si hay un bloque corrupto
    if corruptos:
        print(f"  ¡Bloques corruptos detectados en índices: {corruptos}!")
    else:
        print(" Cadena de bloques íntegra.")

    # Genera un reporte.txt con todos los datos.
    with open('reporte.txt', 'w') as f:
        f.write("===== REPORTE DE BLOCKCHAIN =====\n")
        f.write(f"Total de bloques: {total_bloques}\n")
        f.write(f"Bloques con alerta: {alertas}\n")
        f.write(f"Promedio frecuencia cardíaca: {promedio_frec:.2f}\n")
        f.write(f"Promedio presión sistólica: {promedio_pres:.2f}\n")
        f.write(f"Promedio saturación de oxígeno: {promedio_oxi:.2f}\n")
        if corruptos:
            f.write(f" !Bloques corruptos: {corruptos}\n")
        else:
            f.write(" Cadena íntegra sin errores.\n")

        if detalles_alertas:
            f.write("\nDetalles de alertas:\n")
            for detalle in detalles_alertas:
                f.write(f" - Timestamp: {detalle['timestamp']}\n")
                for alerta in detalle["alertas"]:
                    f.write(f"    * {alerta}\n")
        else:
            f.write("No se detectaron alertas específicas.\n")

    print(" Reporte generado: reporte.txt")

if __name__ == '__main__':
    verificar_blockchain()
