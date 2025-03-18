import argparse

# Función de validación para asegurarse de que el número es positivo
def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s debe ser un número positivo" % value)
    return ivalue

# Crear el parser principal
parser = argparse.ArgumentParser(description="Script con subcomandos y validación")

# Crear los subcomandos
subparsers = parser.add_subparsers(dest='comando')

# Subcomando 1: Aceptar un número positivo y una lista de números
comando1_parser = subparsers.add_parser('comando1', help="Subcomando 1")
comando1_parser.add_argument('numero', type=check_positive, help="Un número positivo")
comando1_parser.add_argument('numeros', type=int, nargs='+', help="Una lista de números")

# Subcomando 2: Aceptar una cadena de texto
comando2_parser = subparsers.add_parser('comando2', help="Subcomando 2")
comando2_parser.add_argument('texto', type=str, help="Una cadena de texto")

# Parsear los argumentos
args = parser.parse_args()

# Lógica para ejecutar según el subcomando elegido
if args.comando == 'comando1':
    print(f"Ejecutando comando1 con número: {args.numero} y lista de números: {args.numeros}")
elif args.comando == 'comando2':
    print(f"Ejecutando comando2 con texto: {args.texto}")
else:
    print("Comando no reconocido")
