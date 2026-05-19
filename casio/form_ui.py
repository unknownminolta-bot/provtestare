# FYXF04 Formelblad
# Korr i Python-laget pa fx-9860GIII
# Skarm: 128x64 px, 21x8 chars
# Texten ar pa svenska men utan a-ring/a-prick/o-prick
# eftersom Casio mini-fonten inte har dessa glyfer.

PAUSE = "  [EXE] forts."


def wait():
    try:
        input(PAUSE)
    except EOFError:
        pass


def p(text):
    lines = text.split("\n")
    for start in range(0, len(lines), 7):
        for line in lines[start:start + 7]:
            print(line)
        if start + 7 < len(lines):
            wait()


def choose(title, items, back="0 Tillbaka"):
    lines = [title] + items + [back]
    for start in range(0, len(lines), 7):
        for line in lines[start:start + 7]:
            print(line)
        if start + 7 < len(lines):
            wait()
    try:
        return input(">")
    except EOFError:
        return "0"

