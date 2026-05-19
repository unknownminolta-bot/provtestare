# Calculator entrypoint. Casio Python launches scripts with:
#   from formler import *
from formmain import all_pages, meny


def main():
    try:
        meny()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__" or __name__ == "formler":
    main()
