import sys


input = sys.stdin.readline

dsc_number: int
discovered: list[int]
is_apoint: list[bool]
edge_list: list[list[int]]


def dfs(node: int, is_root: bool) -> int:
    global dsc_number
    discovered[node] = dsc_number
    dsc_number += 1

    ret: int = discovered[node]
    child: int = 0

    for next_node in edge_list[node]:
        if discovered[next_node] != 0:
            ret = min(ret, discovered[next_node])
            continue

        child += 1
        prev: int = dfs(next_node, False)
        if not is_root and prev >= discovered[node]:
            is_apoint[node] = True
        ret = min(ret, prev)

    if is_root:
        is_apoint[node] = child >= 2

    return ret


def main() -> None:
    global dsc_number, discovered, is_apoint, edge_list
    v, e = map(int, input().split())

    edge_list = [[] for _ in range(v + 1)]
    for _ in range(e):
        _from, _to = map(int, input().split())
        edge_list[_from].append(_to)
        edge_list[_to].append(_from)

    dsc_number = 1
    discovered = [0 for _ in range(v + 1)]
    is_apoint = [False for _ in range(v + 1)]
    for node in range(1, v + 1):
        if discovered[node] == 0:
            dfs(node, True)

    apoint_list: list[int] = sorted(
        node for node, apoint in enumerate(is_apoint) if apoint
    )
    print(len(apoint_list))
    if apoint_list:
        print(" ".join(map(str, apoint_list)))


if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    main()

# reference https://www.crocus.co.kr/1164
