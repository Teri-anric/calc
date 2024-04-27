import sys
from calc.cli import HELP_MESSAGE, main

def _main():
    if "--help" in sys.argv:
        return print(HELP_MESSAGE)
    main()


if __name__ == '__main__':
    _main()