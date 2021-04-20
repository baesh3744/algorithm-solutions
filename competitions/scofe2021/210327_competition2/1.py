from typing import List


def total_time_to_num(time: str) -> int:
    hour, min, sec = map(int, time.split(':'))
    return hour * 3600 + min * 60 + sec


def times_to_num(times: List[str]) -> List[int]:
    int_times: List[int] = []
    for time in times:
        min, sec = map(int, time.split(':'))
        int_times.append(min * 60 + sec)
    return int_times


def solve(total_time: int, times: List[int]) -> List[int]:
    ans: List[int] = [0, 0]
    sum: int = 0
    sidx: int = 0
    for cidx, time in enumerate(times):
        while sum >= total_time:
            sum = sum - times[sidx]
            sidx += 1

        sum += time

        cur_count: int = cidx - sidx + 1
        if ans[0] < cur_count:
            ans = [cur_count, sidx + 1]
    return ans


def main() -> None:
    N, total_time = map(str, input().split())
    times = [input() for _ in range(int(N))]

    count, sidx = solve(total_time_to_num(total_time), times_to_num(times))
    print('{} {}'.format(count, sidx))


if __name__ == "__main__":
    main()
