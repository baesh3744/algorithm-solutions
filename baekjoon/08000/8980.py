import sys


input = sys.stdin.readline


def move(n: int, c: int, box_infos: list[list[tuple[int, int]]]) -> int:
    moved = 0
    truck = [c for _ in range(n + 1)]

    for to_ in range(1, n+1):
        for from_, box in box_infos[to_]:
            capacity = min(box, min(truck[from_:to_]))
            if capacity == 0:
                break

            for index in range(from_, to_):
                truck[index] -= capacity
            moved += capacity

    return moved


def main() -> None:
    n, c = map(int, input().split())
    m = int(input())

    box_infos: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        from_, to_, box = map(int, input().split())
        box_infos[to_].append((from_, box))

    for index, info in enumerate(box_infos):
        box_infos[index] = sorted(info, reverse=True)
    print(move(n, c, box_infos))


if __name__ == "__main__":
    main()
