import sys


ENDTAG = "/"
MAIN = "m"
OPEN_TAG = "<"
CLOSE_TAG = ">"
DIV = "d"
TITLE_RANGE = '"'
P = "p"
END_OF_PTAG = "</p>"
BLANK = " "

input = sys.stdin.readline


def parse_ptag(string: str) -> str:
    istag: bool = False
    length: int = len(string)
    parsed: str = ""

    for idx, char in enumerate(string):
        if char == OPEN_TAG:
            istag = True
        elif char == CLOSE_TAG:
            istag = False
        elif not istag:
            if char == BLANK and (
                len(parsed) == 0 or parsed[-1] == BLANK or idx == length - 1
            ):
                continue
            parsed += char

    return parsed


def parse() -> str:
    index: int = 1
    length: int = len(html)
    parsed: str = ""

    while index < length:
        if html[index] == ENDTAG or html[index] == MAIN:
            index = html.index(CLOSE_TAG, index) + 2

        elif html[index] == DIV:
            start: int = html.index(TITLE_RANGE, index) + 1
            end: int = html.index(TITLE_RANGE, start)
            parsed += f"title : {html[start: end]}\n"
            index = end + 3

        elif html[index] == P:
            end: int = html.index(END_OF_PTAG, index)
            parsed += parse_ptag(html[index + 2 : end]) + "\n"
            index = end + 5

    return parsed


if __name__ == "__main__":
    html = input().strip()

    print(parse().strip())
