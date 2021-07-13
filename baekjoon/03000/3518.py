import sys


def add_space(doc: list[list[str]]) -> list[list[str]]:
    max_cnt_word = max(map(len, doc))
    for word_index in range(max_cnt_word):
        max_word_length = -1
        for line in doc:
            if word_index < len(line):
                max_word_length = max(max_word_length, len(line[word_index]))

        for line_index, line in enumerate(doc):
            if word_index < len(line) - 1:
                doc[line_index][word_index] = line[word_index] \
                    + ' ' * (max_word_length - len(line[word_index]))

    return doc


def main() -> None:
    doc = [line.split() for line in sys.stdin]
    doc = add_space(doc)
    for line in doc:
        print(' '.join(line))


if __name__ == "__main__":
    main()
