import sys


input = sys.stdin.readline


def get_max_value(index: int, weight: int) -> int:
    if index == n:
        return 0
    if cache[index][weight] != -1:
        return cache[index][weight]

    ret: int = 0

    # 현재 물건을 가방에 넣지 않음
    ret = max(ret, get_max_value(index + 1, weight))

    # 현재 물건을 가방에 넣음
    cur_weight, cur_value = items[index]
    next_weight = weight + cur_weight
    if next_weight <= k:
        ret = max(ret, cur_value + get_max_value(index + 1, next_weight))

    cache[index][weight] = ret
    return ret


def main() -> None:
    global n, k, items, cache
    n, k = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(n)]

    # cache[물건 인덱스][현재까지 가방에 넣은 무게]
    cache = [[-1 for _ in range(k + 1)] for _ in range(n)]
    print(get_max_value(0, 0))


if __name__ == "__main__":
    main()
