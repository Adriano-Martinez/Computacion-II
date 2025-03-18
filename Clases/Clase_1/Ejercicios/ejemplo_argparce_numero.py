import argparse

# Crear el parser
parser = argparse.ArgumentParser(description="Procesar un número de entrada.")
parser.add_argument('number', type=int, help="Un número entero")

# Parsear los argumentos
args = parser.parse_args()

# Imprimir el resultado
print(f"Número ingresado: {args.number}")
