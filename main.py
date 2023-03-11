from argparse import ArgumentParser

DEFAULT_NUMBER = 1000000000

def main():
    parser = ArgumentParser()
    parser.add_argument("-n", "--number", dest="number",
                        help="Numbers of strings.", default=DEFAULT_NUMBER)

    args = parser.parse_args()
    print(args.number)

if __name__ == "__main__":
    main()
