from multiprocessing import Process, Pipe

def enviar(conn):
    conn.send("Mensaje desde el hijo")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=enviar, args=(child_conn,))
    p.start()

    print(parent_conn.recv())  # Espera y recibe el mensaje
    p.join()
