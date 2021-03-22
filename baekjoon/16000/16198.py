from typing import List


def get_max_energy(W: List[int], energy: int) -> int:
    if len(W) == 2:
        return energy

    max_energy: int = 0
    for index in range(1, len(W) - 1):
        new_energy: int = energy + W[index - 1] * W[index + 1]
        new_W: List[int] = W[:]
        new_W.pop(index)
        max_energy = max(max_energy, get_max_energy(new_W, new_energy))
    return max_energy


def main() -> None:
    _ = int(input())
    W = list(map(int, input().split()))
    print(get_max_energy(W, 0))


if __name__ == "__main__":
    main()
