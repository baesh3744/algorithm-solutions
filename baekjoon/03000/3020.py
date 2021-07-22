import sys

input = sys.stdin.readline


def count_by_height(max_cnt: int, h: int, obstacles: list[int]) -> list[int]:
    cnt = 0
    cnt_obstacles = [0 for _ in range(h+1)]
    for height in range(h, 0, -1):
        while cnt < max_cnt and height <= obstacles[cnt]:
            cnt += 1
        cnt_obstacles[height] = cnt
    return cnt_obstacles


def count_obstacle(n: int, h: int, obstacles: list[int]) -> tuple[int, int]:
    jong = count_by_height(n//2, h, sorted(obstacles[::2], reverse=True))
    seok = count_by_height(n//2, h, sorted(obstacles[1::2], reverse=True))

    cnt, min_obstacle = 0, sys.maxsize
    for height in range(1, h+1):
        obstacle = jong[height] + seok[(h+1) - height]
        if obstacle < min_obstacle:
            cnt, min_obstacle = 1, obstacle
        elif obstacle == min_obstacle:
            cnt += 1
    return min_obstacle, cnt


def main() -> None:
    n, h = map(int, input().split())
    obstacles = [int(input()) for _ in range(n)]

    min_obstacle, cnt = count_obstacle(n, h, obstacles)
    print(min_obstacle, cnt)


if __name__ == "__main__":
    main()
