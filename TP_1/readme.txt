# Trabajo práctico n°1: Sistema de Monitoreo Biométrico con Blockchain Simple

## Descripción
Este trabajo simula un sistema de monitoreo biométrico en tiempo real que registra señales fisiológicas (frecuencia cardíaca, presión arterial sistólica y saturación de oxígeno). Utiliza procesamiento concurrente con `multiprocessing` para analizar las señales en paralelo y un verificador que genera una cadena de bloques (blockchain) para garantizar la integridad de los datos.

El sistema:
- Genera muestras biométricas aleatorias cada segundo.
- Tres procesos analizadores calculan la media y desviación estándar usando una ventana móvil.
- Un proceso verificador recibe resultados, detecta alertas y construye bloques con hashes encadenados para validar la integridad.
- Guarda la cadena de bloques en un archivo JSON.
- Permite verificar la integridad y generar reportes mediante un script aparte.

## Estructura
- `main.py`: Código principal que genera datos, ejecuta procesos analizadores y verificador.
- `verificar_cadena.py`: Script que verifica la integridad de la cadena de bloques y genera un reporte.
- `blockchain.json`: Archivo generado con la cadena de bloques.
- `reporte.txt`: Archivo con estadísticas y alertas generado tras la verificación.

## Requisitos
- Python 3.x
- Módulos estándar (incluidos en Python):  
  `multiprocessing`, `time`, `random`, `datetime`, `hashlib`, `json`
- Módulo externo:  
  `numpy`

Para instalar `numpy` si no está instalado:

```bash
pip install numpy
```

## Instrucciones
Ejecutar el programa principal para generar y analizar las muestras biométricas:

```bash
python3 main.py
```

Ejecutar el script para verificar la cadena y generar un reporte:

```bash
python3 verificar_cadena.py
```

## Funcionamiento general
- `main.py` crea procesos paralelos para analizar diferentes señales biométricas.
- Cada analizador mantiene una ventana de 30 muestras para calcular estadísticas.
- El verificador espera los resultados, construye bloques encadenados con hashes y detecta alertas.
- La cadena de bloques garantiza que los datos no fueron modificados.
- `verificar_cadena.py` comprueba la integridad del archivo JSON y genera un informe de alertas y promedios.

## Alertas
El sistema marca alerta si:
- Frecuencia cardíaca media ≥ 200 bpm.
- Presión sistólica media ≥ 200 mmHg.
- Saturación de oxígeno media fuera del rango 90-100%.