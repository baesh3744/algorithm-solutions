import sys
from collections import deque


input = sys.stdin.readline


class Person:
    def __init__(self, friends: list[int]) -> None:
        self.cnt_rumor = 0
        self.cnt_friends = len(friends)
        self.time = -1
        self.friends = friends


def spread_rumor(n: int, init_rumor: list[int]) -> None:
    time = 0
    checked = [False for _ in range(n+1)]
    que: deque[int] = deque()

    for init in init_rumor:
        que.append(init)
        checked[init] = True
        graph[init].time = time

    while que:
        time += 1
        for _ in range(len(que)):
            cur_rumor = que.popleft()

            for next_rumor in graph[cur_rumor].friends:
                if not checked[next_rumor]:
                    graph[next_rumor].cnt_rumor += 1

                    person = graph[next_rumor]
                    if 2*person.cnt_rumor >= person.cnt_friends:
                        que.append(next_rumor)
                        checked[next_rumor] = True
                        graph[next_rumor].time = time


def main() -> None:
    global graph
    n = int(input())

    graph = [Person([])]
    for _ in range(n):
        friends = list(map(int, input().split()))
        friends.pop()
        graph.append(Person(friends))

    _ = int(input())
    init_rumor = list(map(int, input().split()))

    spread_rumor(n, init_rumor)
    for person in graph[1:]:
        print(person.time, end=' ')


if __name__ == "__main__":
    main()
