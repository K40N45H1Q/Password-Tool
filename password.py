from sys import argv
from random import choices, shuffle
from string import digits, ascii_letters

def get_password(length):
    charset = list(ascii_letters+digits); shuffle(charset)
    return "".join(choices(charset, k=length))

if __name__ == "__main__":
    if len(argv) == 2:
        try:
            assert argv[-1].isdigit() == True
            if int(argv[-1]) == 0:
                print(get_password(15))
            else:
                print(get_password(int(argv[-1])))
        except AssertionError:
            print("If you specify the length as the first argument, it must be a number.")
    else:
        print(get_password(15))
        