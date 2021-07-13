import sys


def get_proficiency(record: str) -> int:
    proficiency: int = 0
    for rec in record:
        proficiency |= 1 << int(rec)
    return proficiency


def main() -> None:
    n: int = -1
    end_line: int = -1
    proficiencies: list[int] = []
    for lnum, line in enumerate(sys.stdin):
        if n == -1:
            n = int(line)
            end_line = lnum + n
            proficiencies = [0 for _ in range(1024)]
        else:
            proficiencies[get_proficiency(line.strip())] = 1
        if lnum == end_line:
            print(sum(proficiencies))
            n = -1


if __name__ == "__main__":
    main()
