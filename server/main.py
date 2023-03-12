import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


def thread_client(conn):
    while True:
        data = conn.recv(1024)
        print(data)
        conn.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        worker = threading.Thread(target=thread_client, args=(conn,))
        worker.start()
