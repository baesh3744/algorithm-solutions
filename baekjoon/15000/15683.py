import copy
import sys
from collections import deque


#       left  right  top  bottom
# rdir     0      0   -1       1
# cdir    -1      1    0       0
def see_one_direction(office: list[list[int]],
                      ridx: int,
                      cidx: int,
                      rdir: int,
                      cdir: int) -> list[list[int]]:
    while 0 <= ridx < n and 0 <= cidx < m and office[ridx][cidx] != 6:
        if office[ridx][cidx] == 0:
            office[ridx][cidx] = -1
        ridx += rdir
        cidx += cdir
    return office


def see(office: list[list[int]],
        ridx: int,
        cidx: int,
        left: bool,
        right: bool,
        top: bool,
        bottom: bool) -> list[list[int]]:
    seen_office: list[list[int]] = copy.deepcopy(office)
    if left:
        seen_office = see_one_direction(seen_office, ridx, cidx, 0, -1)
    if right:
        seen_office = see_one_direction(seen_office, ridx, cidx, 0, 1)
    if top:
        seen_office = see_one_direction(seen_office, ridx, cidx, -1, 0)
    if bottom:
        seen_office = see_one_direction(seen_office, ridx, cidx, 1, 0)
    return seen_office


def count_blind_area(office: list[list[int]]) -> int:
    blind_area: int = 0
    for ridx in range(n):
        for cidx in range(m):
            if office[ridx][cidx] == 0:
                blind_area += 1
    return blind_area


def get_min_blind_area(office: list[list[int]]) -> int:
    # cctv가 바라보는 방향에 따른 사무실의 상태를 que에 저장
    que: deque[list[list[int]]] = deque()
    que.append(office)

    for ridx in range(n):
        for cidx in range(m):
            status: int = office[ridx][cidx]
            if status == 0 or status == 6:
                continue

            que_size: int = len(que)
            for _ in range(que_size):
                cur_office = que.popleft()
                if status == 1:
                    que.append(  # 좌
                        see(cur_office, ridx, cidx, True, False, False, False))
                    que.append(  # 우
                        see(cur_office, ridx, cidx, False, True, False, False))
                    que.append(  # 상
                        see(cur_office, ridx, cidx, False, False, True, False))
                    que.append(  # 하
                        see(cur_office, ridx, cidx, False, False, False, True))
                elif status == 2:
                    que.append(  # 좌우
                        see(cur_office, ridx, cidx, True, True, False, False))
                    que.append(  # 상하
                        see(cur_office, ridx, cidx, False, False, True, True))
                elif status == 3:
                    que.append(  # 좌상
                        see(cur_office, ridx, cidx, True, False, True, False))
                    que.append(  # 좌하
                        see(cur_office, ridx, cidx, True, False, False, True))
                    que.append(  # 우상
                        see(cur_office, ridx, cidx, False, True, True, False))
                    que.append(  # 우하
                        see(cur_office, ridx, cidx, False, True, False, True))
                elif status == 4:
                    que.append(  # 우상하
                        see(cur_office, ridx, cidx, False, True, True, True))
                    que.append(  # 좌상하
                        see(cur_office, ridx, cidx, True, False, True, True))
                    que.append(  # 좌우하
                        see(cur_office, ridx, cidx, True, True, False, True))
                    que.append(  # 좌우상
                        see(cur_office, ridx, cidx, True, True, True, False))
                elif status == 5:
                    que.append(  # 좌우상하
                        see(cur_office, ridx, cidx, True, True, True, True))

    # 사무실 사각 지대의 최소 크기 구하기
    min_blind_area: int = sys.maxsize

    while que:
        cur_office = que.popleft()
        min_blind_area = min(min_blind_area, count_blind_area(cur_office))

    return min_blind_area


def main() -> None:
    global n, m
    n, m = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(n)]

    print(get_min_blind_area(office))


if __name__ == "__main__":
    main()
