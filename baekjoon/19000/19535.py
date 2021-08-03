import sys


input = sys.stdin.readline


def main() -> None:
    n = int(input())

    degrees: list[int] = [0 for _ in range(n + 1)]
    edges: list[tuple[int, int]] = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
        degrees[u] += 1
        degrees[v] += 1

    du, ga = 0, 0
    for u, v in edges:
        du += (degrees[u]-1) * (degrees[v]-1)
    for node in range(1, n+1):
        if degrees[node] >= 3:
            ga += degrees[node] * (degrees[node]-1) * (degrees[node]-2) // 6

    if du > 3 * ga:
        print('D')
    elif du < 3 * ga:
        print('G')
    else:
        print('DUDUDUNGA')


if __name__ == "__main__":
    main()
