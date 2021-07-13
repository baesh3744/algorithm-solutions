def count_group(score: int, num_problems: list[int]) -> int:
    cnt_group, sum_score = 0, 0
    for problem in num_problems:
        sum_score += problem
        if score <= sum_score:
            cnt_group += 1
            sum_score = 0
    return cnt_group


def get_score(k: int, num_problems: list[int]) -> int:
    start, end = 0, sum(num_problems)
    while start <= end:
        mid: int = (start + end) // 2
        group = count_group(mid, num_problems)
        if k <= group:
            start = mid + 1
        else:
            end = mid - 1
    return end


def main() -> None:
    _, k = map(int, input().split())
    num_problems = list(map(int, input().split()))
    print(get_score(k, num_problems))


if __name__ == "__main__":
    main()
