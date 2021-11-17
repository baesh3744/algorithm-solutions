import sys


input = sys.stdin.readline


def dfs(cow: int) -> bool:
    visited[cow] = True

    for group in wish_list[cow]:
        connected: int = group_list[group]
        if connected == -1 or (not visited[connected] and dfs(connected)):
            cow_list[cow] = group
            group_list[group] = cow
            return True

    return False


if __name__ == "__main__":
    n, m = map(int, input().split())

    wish_list: list[list[int]] = []
    for _ in range(n):
        _, *wishes = map(lambda x: int(x) - 1, input().split())
        wish_list.append(wishes)

    cow_list = [-1 for _ in range(n)]
    group_list = [-1 for _ in range(m)]

    cnt: int = 0
    for cow, group in enumerate(cow_list):
        if group == -1:
            visited = [False for _ in range(n)]
            if dfs(cow):
                cnt += 1
    print(cnt)
