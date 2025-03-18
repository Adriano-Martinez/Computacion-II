import argparse

# Crear el parser de argumentos
parser = argparse.ArgumentParser()

# Definir los argumentos
parser.add_argument('name', help='Tu nombre')
parser.add_argument('--age', type=int, help='Tu edad')

# Parsear los argumentos
args = parser.parse_args()

# Imprimir los valores
print(f'Hola, {args.name}!')
if args.age:
    print(f'Tienes {args.age} años.')
