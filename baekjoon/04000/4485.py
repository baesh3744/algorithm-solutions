import heapq
import sys


MOVE_LIST: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

input = sys.stdin.readline


def dijkstra(n: int, board: list[list[int]]) -> int:
    distances: list[list[int]] = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    heap: list[list[int]] = []

    distances[0][0] = board[0][0]
    heapq.heappush(heap, [distances[0][0], 0, 0])

    while heap:
        cur_distance, cur_ridx, cur_cidx = heapq.heappop(heap)

        if distances[cur_ridx][cur_cidx] < cur_distance:
            continue

        for move_ridx, move_cidx in MOVE_LIST:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx
            if 0 <= next_ridx < n and 0 <= next_cidx < n:
                next_distance: int = cur_distance + board[next_ridx][next_cidx]
                if next_distance < distances[next_ridx][next_cidx]:
                    distances[next_ridx][next_cidx] = next_distance
                    heapq.heappush(heap, [next_distance, next_ridx, next_cidx])

    return distances[n - 1][n - 1]


def main() -> None:
    num: int = 1
    while True:
        n = int(input())
        if n == 0:
            break
        board = [list(map(int, input().split())) for _ in range(n)]
        print(f"Problem {num}:", dijkstra(n, board))
        num += 1


if __name__ == "__main__":
    main()
