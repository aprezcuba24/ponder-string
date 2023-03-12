import logging
import multiprocessing
import socket
import string
from argparse import ArgumentParser, BooleanOptionalAction

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
DOUBLE_A = 1000


def ponder(string_value):
    logging.debug(f"Processing => {string_value}")
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
        if i > 0 and [string_value[i].lower(), string_value[i - 1].lower()] == [
            "a",
            "a",
        ]:
            logging.info(f"Double 'a' rule detected >> '{string_value}'")
            return DOUBLE_A
    value = letters * 1.5 + digits * 2
    return value / spaces if spaces else value


def thread_client(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            continue
        value = ponder(data.decode())
        conn.sendall(bytes(str(value), "utf-8"))


def get_arguments():
    parser = ArgumentParser()
    parser.add_argument(
        "--verbose",
        dest="verbose",
        help="Show more logs.",
        default=False,
        action=BooleanOptionalAction,
    )
    return parser.parse_args()


# I don't want to share this code between client and server because they can be two different applications.
def set_logging(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level)
    logging.info("Start processing")


def main():
    arguments = get_arguments()
    set_logging(arguments.verbose)
    workers = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        try:
            while True:
                conn, addr = s.accept()
                logging.info(f"Connected by {addr}")
                worker = multiprocessing.Process(target=thread_client, args=(conn,))
                worker.start()
                workers.append(worker)
        except KeyboardInterrupt:
            logging.debug(f"Closing workers {len(workers)}")
            for worker in workers:
                worker.terminate()


if __name__ == "__main__":
    main()
