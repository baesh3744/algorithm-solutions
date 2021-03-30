from typing import Final, List


MOD: Final[int] = 9901


def place_lions(N: int) -> int:
    lions: List[List[int]] = [[1, 0, 0], [1, 1, 1]]

    for len in range(2, N + 1):
        pre_idx: int = (len - 1) % 2
        cur_idx: int = len % 2

        lions[cur_idx][0] = (sum(lions[pre_idx])) % MOD
        lions[cur_idx][1] = (lions[pre_idx][0] + lions[pre_idx][2]) % MOD
        lions[cur_idx][2] = (lions[pre_idx][0] + lions[pre_idx][1]) % MOD
    return sum(lions[N % 2]) % MOD


def main() -> None:
    N = int(input())
    print(place_lions(N))


if __name__ == "__main__":
    main()
