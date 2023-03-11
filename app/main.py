import random
import string
import time
from argparse import ArgumentParser

DEFAULT_NUMBER = 1000000000


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


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-n",
        "--number",
        dest="number",
        help="Numbers of strings.",
        default=DEFAULT_NUMBER,
    )
    default_filename = f'files/{time.strftime("%Y%m%d-%H%M%S")}.txt'
    parser.add_argument(
        "-f",
        "--file",
        dest="filename",
        help="Name of the file.",
        default=default_filename,
    )
    args = parser.parse_args()
    write_file(args.filename, args.number)

    value = get_random_string()
    print(value)


if __name__ == "__main__":
    main()
