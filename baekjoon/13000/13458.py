from typing import List
import math


def get_min_viewer(A: List[int], B: int, C: int) -> int:
    viewer: int = 0
    for people in A:
        people -= B
        viewer += 1
        if people > 0:
            viewer += math.ceil(people / C)
    return viewer


def main() -> None:
    _ = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    print(get_min_viewer(A, B, C))


if __name__ == "__main__":
    main()
