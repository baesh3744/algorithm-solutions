import sys


input = sys.stdin.readline


def play(case: int, kidx: int, midx: int, score: list[int], jiwoo: list[bool]) -> int:
    if k in score:
        return int(score.index(k) == 0)

    if case == 1:  # 경희 vs 민호
        next_score = score[:]

        res: int = rel_board[kyunghee[kidx]][minho[midx]]
        winner: int = 1 if res == 2 else 2
        next_case: int = 2 if res == 2 else 3
        next_score[winner] += 1

        return play(next_case, kidx + 1, midx + 1, next_score, jiwoo)

    elif case == 2:  # 지우 vs 경희
        for _jiwoo, is_used in enumerate(jiwoo):
            if not is_used:
                next_jiwoo, next_score = jiwoo[:], score[:]

                res: int = rel_board[_jiwoo][kyunghee[kidx]]
                winner: int = 0 if res == 2 else 1
                next_case: int = 3 if res == 2 else 1
                next_score[winner] += 1
                next_jiwoo[_jiwoo] = True

                if play(next_case, kidx + 1, midx, next_score, next_jiwoo) == 1:
                    return 1

    else:  # 지우 vs 민호
        for _jiwoo, is_used in enumerate(jiwoo):
            if not is_used:
                next_jiwoo, next_score = jiwoo[:], score[:]

                res: int = rel_board[_jiwoo][minho[midx]]
                winner: int = 0 if res == 2 else 2
                next_case: int = 2 if res == 2 else 1
                next_score[winner] += 1
                next_jiwoo[_jiwoo] = True

                if play(next_case, kidx, midx + 1, next_score, next_jiwoo) == 1:
                    return 1

    return 0


def main() -> None:
    global k, rel_board, kyunghee, minho
    n, k = map(int, input().split())
    rel_board = [list(map(int, input().split())) for _ in range(n)]
    kyunghee = list(map(lambda x: int(x) - 1, input().split()))
    minho = list(map(lambda x: int(x) - 1, input().split()))

    print(play(2, 0, 0, [0, 0, 0], [False for _ in range(n)]))


if __name__ == "__main__":
    main()
