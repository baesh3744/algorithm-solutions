def main() -> None:
    w, _ = map(int, input().split())
    a = list(map(int, input().split()))

    has_answer: bool = False
    cache = [False for _ in range(1000000)]
    for pivot, pnum in enumerate(a):
        for num in a[pivot + 1 :]:
            if pnum + num > w:
                continue
            if cache[w - pnum - num]:
                has_answer = True
                break
        if has_answer:
            break
        for num in a[:pivot]:
            if pnum + num < w:
                cache[pnum + num] = True
    print("YES" if has_answer else "NO")


if __name__ == "__main__":
    main()

# Reference https://skyde47.tistory.com/39
