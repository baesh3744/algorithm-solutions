from typing import List, Set, Tuple


def get_not_heard_and_seen(not_heard: List[str], not_seen: List[str]) -> Tuple[int, List[str]]:
    not_heard_as_set: Set[str] = set(not_heard)
    intersection: Set[str] = not_heard_as_set.intersection(not_seen)
    intersection_as_list: List[str] = list(intersection)
    return len(intersection_as_list), sorted(intersection_as_list)


def main() -> None:
    N, M = map(int, input().split())
    not_heard = [input() for _ in range(N)]
    not_seen = [input() for _ in range(M)]

    count, ilist = get_not_heard_and_seen(not_heard, not_seen)
    print(count)
    for person in ilist:
        print(person)


if __name__ == "__main__":
    main()
