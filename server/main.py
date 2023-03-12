import logging
import socket
import string
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
DOUBLE_A = 1000


def ponder(string_value):
    letters = 0
    digits = 0
    spaces = 0
    for i in range(0, len(string_value)):
        if string_value[i] in string.ascii_letters:
            letters += 1
        if string_value[i] in string.digits:
            digits += 1
        if string_value[i] == " ":
            spaces += 1
        if (
            i > 0
            and string_value[i].lower() == "a"
            and string_value[i - 1].lower() == "a"
        ):
            logging.info(f"Double 'a' rule detected >> '{string_value}'")
            return DOUBLE_A
    value = letters * 1.5 + digits * 2
    return value / spaces if spaces else value


def thread_client(conn):
    while True:
        data = conn.recv(1024)
        print(data)
        conn.sendall(data)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            worker = threading.Thread(target=thread_client, args=(conn,))
            worker.start()


if __name__ == "__main__":
    main()
