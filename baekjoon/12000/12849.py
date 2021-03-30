from typing import Final, List


MOD: Final[int] = 1000000007


def get_path_count(D: int) -> int:
    # cache[D][hall] - D분일 때, hall에 위치하는 경우의 수
    # 0 정보과학관      4 환경직기념관
    # 1 전산관          5 진리관
    # 2 미래관          6 학생회관
    # 3 신양관          7 형남공학관
    cache: List[List[int]] = [[0 for _ in range(8)] for _ in range(D + 1)]
    paths: List[List[int]] = [[1, 2], [0, 2, 3], [0, 1, 3, 4],
                              [1, 2, 4, 5], [2, 3, 5, 7], [3, 4, 6], [5, 7], [4, 6]]

    for d in range(D + 1):
        if d == 0:
            cache[d][0] = 1
        else:
            for cur_hall, next_halls in enumerate(paths):
                for next_hall in next_halls:
                    cache[d][cur_hall] += cache[d - 1][next_hall]
                cache[d][cur_hall] %= MOD
    return cache[D][0]


def main() -> None:
    D = int(input())

    print(get_path_count(D))


if __name__ == "__main__":
    main()
