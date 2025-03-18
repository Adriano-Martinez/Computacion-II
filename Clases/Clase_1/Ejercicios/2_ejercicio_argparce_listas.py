import argparse

# Crear el parser
parser = argparse.ArgumentParser(description="Procesar una lista de números y calcular su suma.")
parser.add_argument('numbers', type=int, nargs='+', help="Una lista de números enteros")

# Parsear los argumentos
args = parser.parse_args()

# Calcular la suma de los números
suma = sum(args.numbers)

# Imprimir el resultado
print(f"La suma de los números es: {suma}")
