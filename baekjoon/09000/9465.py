import sys


input = sys.stdin.readline


def get_score(select_type: int, index: int) -> int:
    if index == n + 1:
        return 0
    if cache[select_type][index] != -1:
        return cache[select_type][index]

    score: int = 0
    if select_type == 2:
        for next_type in range(3):
            score = max(score, get_score(next_type, index + 1))
    else:
        for next_type in range(3):
            if next_type != select_type:
                score = max(score, get_score(next_type, index + 1))
        score += stickers[select_type][index]

    cache[select_type][index] = score
    return score


def main() -> None:
    global n, stickers, cache
    t = int(input())
    for _ in range(t):
        n = int(input())
        stickers = [[0] + list(map(int, input().split())) for _ in range(2)]

        # cache[스티커 선택 타입][스티커 인덱스]
        # 스티커 선택 타입: 0 - 위, 1 - 아래, 2 - 선택x
        cache = [[-1 for _ in range(n + 1)] for _ in range(3)]

        print(get_score(2, 0))


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    main()
