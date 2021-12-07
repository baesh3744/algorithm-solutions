import sys
from heapq import heappop, heappush


input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())

    difficult_orders: list[tuple[int, int]] = []
    easy_orders: list[tuple[int, int]] = []
    levels: dict[int, int] = dict()
    for _ in range(n):
        p, l = map(int, input().split())
        levels[p] = l
        heappush(difficult_orders, (-l, -p))
        heappush(easy_orders, (l, p))

    removed: set[tuple[int, int]] = set()
    m = int(input())
    for _ in range(m):
        cmd, *params = input().split()

        if cmd == "recommend":
            x = int(params[0])
            if x == 1:
                if difficult_orders[0] in removed:
                    heappop(difficult_orders)
                print(-difficult_orders[0][1])
            else:
                if easy_orders[0] in removed:
                    heappop(easy_orders)
                print(easy_orders[0][1])
        elif cmd == "add":
            p, l = map(int, params)
            levels[p] = l
            heappush(difficult_orders, (-l, -p))
            heappush(easy_orders, (l, p))
        else:
            p = int(params[0])
            removed.add((levels[p], p))
            removed.add((-levels[p], -p))
