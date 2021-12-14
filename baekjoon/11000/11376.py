import sys
from typing import List


input = sys.stdin.readline


def match(person: int) -> bool:
    visited[person] = True

    for work in links[person]:
        pic: int = people[work]  # person_in_charge
        if pic == -1 or (not visited[pic] and match(pic)):
            people[work] = person
            works[person] = work
            return True

    return False


if __name__ == "__main__":
    n, m = map(int, input().split())

    links: List[List[int]] = [[] for _ in range(2 * n)]
    for person in range(n):
        _, *linked = map(int, input().split())
        links[2 * person] = linked
        links[2 * person + 1] = linked

    # people[work] = person --> 일(work)를 수행하는 사람(person)
    people: List[int] = [-1 for _ in range(m + 1)]
    # works[person] = work --> 사람(person)이 담당하는 일(work)
    works: List[int] = [-1 for _ in range(2 * n)]

    cnt: int = 0
    for person in range(2 * n):
        if works[person] == -1:
            visited: List[bool] = [False for _ in range(2 * n)]
            cnt += match(person)
    print(cnt)
