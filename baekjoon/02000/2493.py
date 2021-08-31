def get_received_list(n: int, tower_list: list[int]) -> list[int]:
    received_list: list[int] = [0 for _ in range(n)]
    stack: list[tuple[int, int]] = []

    for index, tower in enumerate(tower_list):
        while stack and stack[-1][1] <= tower:
            lower, _ = stack.pop()
            if stack:
                received_list[lower] = stack[-1][0] + 1
        stack.append((index, tower))
    while stack:
        index, _ = stack.pop()
        if stack:
            received_list[index] = stack[-1][0] + 1
    return received_list


def main() -> None:
    n = int(input())
    tower_list = list(map(int, input().split()))

    print(" ".join(map(str, get_received_list(n, tower_list))))


if __name__ == "__main__":
    main()
