from typing import List


MAX: int = 100000


def is_range(row: int, col: int) -> bool:
    return 0 <= row and row < M and 0 <= col and col < N


def find_shortest_path(row: int, col: int, count: int) -> int:
    if row == M - 1:
        return count

    visited[row][col] = count
    move_array: List[List[int]] = [[0, 1], [1, 0], [0, -1]]
    shortest_move: int = MAX
    for index, move in enumerate(move_array):
        next_row: int = row + move[0]
        next_col: int = col + move[1]
        next_count: int = count if index == 1 else count + 1

        if (is_range(next_row, next_col)
            and screen[next_row][next_col] == '.'
                and visited[next_row][next_col] == -1):
            shortest_move = min(shortest_move, find_shortest_path(
                next_row, next_col, next_count))
    return shortest_move


def main() -> None:
    global N, M, screen, visited
    N, M = map(int, input().split())
    screen = [[ch for ch in input()] for _ in range(M)]

    ans: int = MAX
    for col, value in enumerate(screen[0]):
        if value == 'c':
            visited = [[-1 for _ in range(N)] for _ in range(M)]
            count = find_shortest_path(0, col, 0)
            ans = min(ans, count)
    print(ans) if ans != MAX else print('-1')


if __name__ == "__main__":
    main()
