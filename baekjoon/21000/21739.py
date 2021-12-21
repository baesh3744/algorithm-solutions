import sys
from math import factorial


MOD = 1_000_000_007
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())

    catalan_number: int = factorial(2 * n) // (factorial(n) * factorial(n + 1))
    print(catalan_number % MOD)
