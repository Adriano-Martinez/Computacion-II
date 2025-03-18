import getopt
import sys

# Lista de opciones que aceptamos (en este caso, -f para un archivo y -v para activar verbose)
opts, args = getopt.getopt(sys.argv[1:], 'f:v')

# Procesamos los argumentos
for opt, arg in opts:
    if opt == '-f':
        print(f"Archivo: {arg}")
    elif opt == '-v':
        print("Modo verbose activado.")
