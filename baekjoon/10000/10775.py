import sys


cache: list[int] = []


def find(gate: int) -> int:
    if cache[gate] == gate:
        return gate
    cache[gate] = find(cache[gate])
    return cache[gate]


def union(x: int, y: int) -> None:
    x = find(x)
    y = find(y)
    cache[y] = x


def count_plane(gates: list[int]) -> int:
    cnt: int = 0
    for gate in gates:
        docking = find(gate)
        if docking == 0:
            break
        cnt += 1
        union(docking - 1, docking)
    return cnt


def main() -> None:
    global cache
    g = int(input())
    p = int(input())
    gates = [int(sys.stdin.readline()) for _ in range(p)]

    cache = [num for num in range(g + 1)]
    print(count_plane(gates))


if __name__ == "__main__":
    main()
