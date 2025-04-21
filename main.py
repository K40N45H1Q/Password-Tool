from src.ascii import art
from os import system, name
from getpass import getpass
from argparse import ArgumentParser
from random import choices, shuffle
from src.dcclib import DynamicCenteredConsole
from string import digits, ascii_letters, punctuation

class PasswordUtility:

    VERSSION = "\nVERSSION 1.1.0 by @github.com/K40N45H1Q"
    DESCRIPTION = "\nThe simplest utility for generate passwords\n"

    def __init__(self):
        self.__charset = []
        self.__ascii_art = art
        self.__dcc = DynamicCenteredConsole()
        self.__parser = ArgumentParser(description=self.DESCRIPTION)
        self.__arguments = self.__configure_and_parse()

    def __configure_and_parse(self):
        self.__parser.add_argument(
            "--length", "-l",
            type=int,
            nargs="?",
            default=45,
            help="Length of each password (default is 45)"
        )

        self.__parser.add_argument(
            "--quantity", "-q",
            type=int,
            nargs="?",
            default=10,
            help="Quantity of passwords to generate (default is 10)"
        )

        self.__parser.add_argument(
            "--difficulty", "-d",
            type=int,
            nargs="?",
            default=3,
            help="Password difficulty, ranging from 1 to 3 (default is the maximum)"
        )

        return self.__parser.parse_args()

    def main(self):
        print("\033[1;32m")
        if self.__arguments.quantity <= 32 and self.__arguments.length <= 45:
            __passwords = []
            for _ in range(self.__arguments.quantity):
                shuffle(self.__charset)
                __passwords.append("".join(
                    choices(
                        digits if self.__arguments.difficulty == 1 else
                        digits + ascii_letters if self.__arguments.difficulty == 2 else
                        digits + ascii_letters + punctuation,
                        k=self.__arguments.length if self.__arguments.length > 0 else 15
                    )
                )
            )
            self.__dcc.update(f"{self.__ascii_art}\n{self.DESCRIPTION}")
            self.__dcc.update(__passwords); self.__dcc.update(self.VERSSION)
            self.__dcc.update(f"\033[1;31m\n[ PRESS ANY KEY TO EXIT ]\n\033[0m")
        getpass(prompt=""); system("clear") if name != "nt" else system("cls"); return 0

if __name__ == "__main__":
    PasswordUtility().main()