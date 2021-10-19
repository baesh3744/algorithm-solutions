import sys


input = sys.stdin.readline

cache: list[int]


def union(x: int, y: int) -> None:
    x, y = cache[x], cache[y]
    if x > y:
        x, y = y, x

    if x != y:
        for person, group in enumerate(cache):
            if group == y:
                cache[person] = x


def main() -> None:
    global cache
    n, m = map(int, input().split())

    cache = [num for num in range(n + 1)]
    true_people = list(map(int, input().split()))
    for person in true_people[1:]:
        cache[person] = 0

    party_list = [list(map(int, input().split())) for _ in range(m)]
    for party in party_list:
        first: int = party[1]
        for person in party[2:]:
            union(first, person)

    ans: int = 0
    for party in party_list:
        can_lie: bool = True
        for person in party[1:]:
            if cache[person] == 0:
                can_lie = False
                break
        ans += int(can_lie)
    print(ans)


if __name__ == "__main__":
    main()
