import random
import string
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
        result_str = result_str[:pos] + " " + result_str[pos + 1:]
    return result_str


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-n",
        "--number",
        dest="number",
        help="Numbers of strings.",
        default=DEFAULT_NUMBER,
    )

    args = parser.parse_args()
    value = get_random_string()
    print(value)


if __name__ == "__main__":
    main()
