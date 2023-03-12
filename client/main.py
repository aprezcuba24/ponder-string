import logging
import os
import random
import socket
import string
from argparse import ArgumentParser

DEFAULT_NUMBER = 1000000000
DEFAULT_NUMBER = 100
HOST = "127.0.0.1"
PORT = 65432
CHAIN_FILE = "chains.txt"
CHAIN_RESPOND_FILE = "chains_respond.txt"


def get_random_string():
    length = random.randrange(50, 100)
    characters = string.ascii_letters + string.digits
    result_str = "".join(random.choice(characters) for i in range(length))
    selected = [0, length]
    for i in range(0, random.randrange(3, 5)):
        pos = random.choice([ele for ele in range(0, length) if ele not in selected])
        selected += [pos, pos + 1, pos - 1]
        result_str = result_str[:pos] + " " + result_str[pos + 1 :]
    return result_str


def write_file(filename, number_lines):
    with open(filename, "w+") as f:
        for i in range(0, number_lines):
            f.write(f"{get_random_string()}\n")


def read_file(filename):
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield line.strip()


def process_file(filename_in, filename_out):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s, open(
        filename_out, "w+"
    ) as f:
        s.connect((HOST, PORT))
        for line in read_file(filename_in):
            s.send(bytes(line, "utf-8"))
            data = s.recv(1024)
            value = float(data.decode())
            f.write(f"{value}\n")


def main():
    cwd = os.getcwd()
    parser = ArgumentParser()
    parser.add_argument(
        "-n",
        "--number",
        dest="number",
        help="Numbers of strings.",
        default=DEFAULT_NUMBER,
    )
    parser.add_argument(
        "-f",
        "--file",
        dest="filename",
        help="Name of the file.",
        default=f"{cwd}/{CHAIN_FILE}",
    )
    parser.add_argument(
        "-r",
        "--file-respond",
        dest="filename_respond",
        help="Name of the file.",
        default=f"{cwd}/{CHAIN_RESPOND_FILE}",
    )
    arguments = parser.parse_args()
    if arguments.filename_respond == arguments.filename:
        logging.error("The respond file should be different to filename")
        return

    write_file(arguments.filename, arguments.number)
    process_file(arguments.filename, arguments.filename_respond)


if __name__ == "__main__":
    main()
