def get_operation_count(start: int, end: int) -> int:
    if start == end:
        return 0
    if start + 1 == end:
        return matrix[start][0] * matrix[start][1] * matrix[end][1]
    if cache[start][end] != -1:
        return cache[start][end]

    opcount: int = 2 ** 31
    for mid in range(start, end):
        collapse_count: int = (matrix[start][0]
                               * matrix[mid][1]
                               * matrix[end][1])
        opcount = min(opcount, (get_operation_count(start, mid)
                                + get_operation_count(mid + 1, end)
                                + collapse_count))
    cache[start][end] = opcount
    return opcount


def main() -> None:
    global matrix, cache
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    cache = [[-1 for _ in range(n)] for _ in range(n)]

    print(get_operation_count(0, n - 1))


if __name__ == "__main__":
    main()
