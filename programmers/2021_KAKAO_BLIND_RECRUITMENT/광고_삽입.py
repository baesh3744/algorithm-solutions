from typing import List


def to_number(time: str) -> int:
    num: int = 0
    for splitted in time.split(":"):
        num = (60 * num) + int(splitted)
    return num


def to_time(num: int) -> str:
    hour: int = num // 3600
    min: int = (num % 3600) // 60
    sec: int = num % 60
    return f"{hour:02}:{min:02}:{sec:02}"


def solution(play_time: str, adv_time: str, logs: List[str]):
    play: int = to_number(play_time)
    adv: int = to_number(adv_time)
    time_zone: List[int] = [0 for _ in range(360000)]

    for log in logs:
        start, end = map(to_number, log.split("-"))
        time_zone[start] += 1
        time_zone[end] -= 1

    for time in range(1, play + 1):
        time_zone[time] += time_zone[time - 1]

    for time in range(1, play + 1):
        time_zone[time] += time_zone[time - 1]

    answer: int = 0
    max_time: int = time_zone[adv]
    for start in range(1, to_number(play_time) - adv + 1):
        time: int = time_zone[start + adv] - time_zone[start]
        if time > max_time:
            answer = start + 1
            max_time = time
    return to_time(answer)


# "01:30:59"
print(
    solution(
        "02:03:55",
        "00:14:15",
        [
            "01:20:15-01:45:14",
            "00:40:31-01:00:00",
            "00:25:50-00:48:29",
            "01:30:59-01:53:29",
            "01:37:44-02:02:30",
        ],
    )
)
# "01:00:00"
print(
    solution(
        "99:59:59",
        "25:00:00",
        [
            "69:59:59-89:59:59",
            "01:00:00-21:00:00",
            "79:59:59-99:59:59",
            "11:00:00-31:00:00",
        ],
    )
)
# "00:00:00"
print(
    solution(
        "50:00:00",
        "50:00:00",
        ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"],
    )
)
