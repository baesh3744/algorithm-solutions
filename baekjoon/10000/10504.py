import sys


input = sys.stdin.readline


def divide(N: int) -> list[int]:
    for n in range(2, int((2 * N) ** 0.5) + 1):
        if 2 * N % n == 0 and (exp := ((2 * N) // n - n + 1)) % 2 == 0:
            start: int = exp // 2
            return [num for num in range(start, start + n)]
    return []


def to_equation(N: int, expression: list[int]) -> str:
    eq: str = f"{N} = "
    for num in expression:
        eq += f"{num} + "
    return eq[:-3]


def main() -> None:
    t = int(input())
    for _ in range(t):
        N = int(input())
        numbers = divide(N)
        print(to_equation(N, numbers) if numbers else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
