from typing import List


def main() -> None:
    N: int
    M: int
    N, M = map(int, input().split())
    A: List[int] = list(map(int, input().split()))

    a: int
    sum: int = 0
    answer: int = 0
    start_idx: int = 0
    for a in A:
        sum += a
        while(sum > M):
            sum -= A[start_idx]
            start_idx += 1
        if(sum == M):
            answer += 1
    print(answer)


if __name__ == "__main__":
    main()
