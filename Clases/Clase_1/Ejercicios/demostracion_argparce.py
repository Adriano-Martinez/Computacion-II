import argparse

def main():
    # Crear el parser de argumentos
    parser = argparse.ArgumentParser(description="Procesa un archivo y activa el modo verbose si se indica.")
    
    # Definir los argumentos
    parser.add_argument('-f', '--file', help="Archivo de entrada", required=True)
    parser.add_argument('-v', '--verbose', help="Activar modo verbose", action='store_true')

    # Parsear los argumentos
    args = parser.parse_args()

    # Mostrar resultados
    if args.verbose:
        print("Modo verbose activado.")
    print(f"Archivo de entrada: {args.file}")

if __name__ == "__main__":
    main()
