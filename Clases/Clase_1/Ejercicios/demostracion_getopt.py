import getopt
import sys

def main():
    # Analizar los argumentos pasados al script
    opts, args = getopt.getopt(sys.argv[1:], 'f:v')
    
    archivo = None
    verbose = False
    
    for opt, arg in opts:
        if opt == '-f':
            archivo = arg
        elif opt == '-v':
            verbose = True
    
    # Mostrar resultados
    if verbose:
        print("Modo verbose activado.")
    if archivo:
        print(f"Archivo de entrada: {archivo}")
    else:
        print("No se proporcionó un archivo.")

if __name__ == "__main__":
    main()
