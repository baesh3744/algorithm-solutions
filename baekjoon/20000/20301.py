import sys
from collections import deque


def josephus(k: int, m: int, dir: int, people: deque[int]) -> list[int]:
    sequence: list[int] = []
    for _ in range(m):
        if not people:
            return sequence
        people.rotate(dir * (k - 1))
        if dir == -1:
            sequence.append(people.popleft())
        else:
            sequence.append(people.pop())
    return sequence + josephus(k, m, -1 * dir, people)


def main() -> None:
    n, k, m = map(int, input().split())

    people = deque([person for person in range(1, n + 1)])
    print("\n".join(map(str, josephus(k, m, -1, people))))


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
