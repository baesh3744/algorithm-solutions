def main() -> None:
    _ = int(input())
    files = sorted(map(int, input().split()))

    cnt: int = 0
    smaller_idx: int = 0
    for idx, value in enumerate(files):
        while files[smaller_idx] < 0.9 * value:
            smaller_idx += 1
        cnt += idx - smaller_idx
    print(cnt)


if __name__ == "__main__":
    main()
