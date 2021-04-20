from typing import List, Tuple


def get_max_score(n: int, assignments: List[Tuple[int, int]]) -> int:
    scores: List[int] = [0 for _ in range(n + 1)]

    assignments.sort(key=lambda x: x[1], reverse=True)

    for d, w in assignments:
        for day in range(d, 0, -1):
            if day <= n and scores[day] == 0:
                scores[day] = w
                break

    return sum(scores)


def main() -> None:
    n = int(input())
    assignments: List[Tuple[int, int]] = []
    for _ in range(n):
        d, w = map(int, input().split())
        assignments.append((d, w))

    print(get_max_score(n, assignments))


if __name__ == "__main__":
    main()
