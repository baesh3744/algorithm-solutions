from typing import List


def get_three_solutions(solutions: List[int]) -> List[int]:
    ans: List[int] = []
    dist: int = 3000000000

    for base in range(len(solutions) - 2):
        start: int = base + 1
        end: int = len(solutions) - 1

        while start < end:
            mixed: int = solutions[base] + solutions[start] + solutions[end]
            if abs(mixed) < dist:
                ans = [solutions[base], solutions[start], solutions[end]]
                dist = abs(mixed)
            if mixed < 0:
                start += 1
            else:
                end -= 1

    return ans


def main() -> None:
    _ = int(input())
    solutions = list(map(int, input().split()))

    solution1, solution2, solution3 = get_three_solutions(sorted(solutions))
    print(solution1, solution2, solution3)


if __name__ == "__main__":
    main()
