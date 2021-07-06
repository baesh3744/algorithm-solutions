import bisect


def list2dict(mylist: list[int]) -> dict[int, int]:
    mydict: dict[int, int] = {}
    for index, value in enumerate(mylist):
        mydict[value] = index
    return mydict


def match(switches: list[int], light_bulbs: list[int]) -> list[int]:
    bulb_dict = list2dict(light_bulbs)

    matchings: list[int] = []
    for switch in switches:
        matchings.append(bulb_dict[switch])
    return matchings


def get_lis_length(matchings: list[int]) -> tuple[int, list[int]]:
    lis: list[int] = []
    lis_indexes: list[int] = []
    for value in matchings:
        if len(lis) == 0 or lis[-1] < value:
            lis_indexes.append(len(lis))
            lis.append(value)
        else:
            index: int = bisect.bisect_left(lis, value)
            lis_indexes.append(index)
            lis[index] = value
    return len(lis), lis_indexes


def get_lis(n: int, matchings: list[int]) -> tuple[int, list[int]]:
    lis_length, lis_indexes = get_lis_length(matchings)

    lis: list[int] = [-1 for _ in range(lis_length)]
    idx: int = lis_length - 1
    for pointer in range(n - 1, -1, -1):
        if lis_indexes[pointer] == idx:
            lis[idx] = matchings[pointer]
            idx -= 1
    return lis_length, lis


def main() -> None:
    n = int(input())
    switches = list(map(int, input().split()))
    light_bulbs = list(map(int, input().split()))

    matchings = match(switches, light_bulbs)
    lis_length, lis = get_lis(n, matchings)

    print(lis_length)
    print(' '.join(sorted(map(lambda x: str(light_bulbs[x]), lis))))


if __name__ == "__main__":
    main()
