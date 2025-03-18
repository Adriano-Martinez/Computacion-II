import argparse

# Crear el parser
parser = argparse.ArgumentParser(description="Procesar un archivo de entrada y salida.")
parser.add_argument('input_file', type=str, help="El archivo de entrada")
parser.add_argument('--output_file', type=str, default='salida.txt', help="El archivo de salida")

# Parsear los argumentos
args = parser.parse_args()

# Imprimir los resultados
print(f"Archivo de entrada: {args.input_file}")
print(f"Archivo de salida: {args.output_file}")
