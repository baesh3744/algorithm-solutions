from typing import List


def get_two_solutions(solutions: List[int]) -> List[int]:
    ans: List[int] = []
    dist: int = 2000000000
    start: int = 0
    end: int = len(solutions) - 1

    while start < end:
        mixed: int = solutions[start] + solutions[end]
        if abs(mixed) < dist:
            ans = [solutions[start], solutions[end]]
            dist = abs(mixed)
        if mixed < 0:
            start += 1
        else:
            end -= 1

    return ans


def main() -> None:
    _ = int(input())
    solutions = list(map(int, input().split()))

    solution1, solution2 = get_two_solutions(solutions)
    print(solution1, solution2)


if __name__ == "__main__":
    main()
