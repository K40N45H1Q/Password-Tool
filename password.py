import argparse
from random import choices, shuffle
from string import digits, ascii_letters, punctuation


def get_password(length):
    charset = list(ascii_letters + digits + punctuation)
    shuffle(charset)
    return "".join(choices(charset, k=length))


def main():
    parser = argparse.ArgumentParser(
        description=(
            "generate random passwords.\n"
            "developer: https://github.com/wh0syx"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "length",
        type=int,
        nargs="?",
        default=20,
        help="length of each password. Default is 20 if not specified."
    )

    parser.add_argument(
        "count",
        type=int,
        nargs="?",
        default=7,
        help="number of passwords to generate. Default is 7 if not specified."
    )

    args = parser.parse_args()

    if args.length <= 0:
        args.length = 15

    for _ in range(args.count):
        print("\n" + get_password(args.length))

    print()


if __name__ == "__main__":
    main()
