import sys


NOT_USING = 1000

input = sys.stdin.readline


def get_removing(idx: int, plugged: set[int]) -> int:
    next_usings: list[tuple[int, int]] = []

    for app in plugged:
        try:
            next_usings.append((apps.index(app, idx + 1), app))
        except ValueError:
            next_usings.append((NOT_USING, app))

    next_usings.sort()
    return next_usings[-1][1]


def count() -> int:
    cnt: int = 0
    plugged: set[int] = set()

    for idx, app in enumerate(apps):
        if app in plugged:
            continue

        if len(plugged) == n:
            cnt += 1
            plugged.remove(get_removing(idx, plugged))
        plugged.add(app)

    return cnt


if __name__ == "__main__":
    n, k = map(int, input().split())
    apps = list(map(int, input().split()))

    print(count())
