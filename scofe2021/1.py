from typing import List

start_times: List[str] = []
end_times: List[str] = []


def parse_times(times: List[str]) -> None:
    global start_times, end_times
    for time in times:
        start_time, end_time = time.split(' ~ ')
        start_times.append(start_time)
        end_times.append(end_time)


def get_latest_start_time() -> str:
    ret: str = '00:00'
    for start_time in start_times:
        if ret < start_time:
            ret = start_time
    return ret


def get_earliest_end_time() -> str:
    ret: str = '23:59'
    for end_time in end_times:
        if end_time < ret:
            ret = end_time
    return ret


def main() -> None:
    N = int(input())
    times = [input() for _ in range(N)]

    parse_times(times)

    latest_start_time = get_latest_start_time()
    earliest_end_time = get_earliest_end_time()

    print('{} ~ {}'.format(latest_start_time, earliest_end_time)
          ) if latest_start_time <= earliest_end_time else print('-1')


if __name__ == "__main__":
    main()
