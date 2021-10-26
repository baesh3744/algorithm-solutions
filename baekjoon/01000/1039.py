def swap(string: str, i: int, j: int) -> str:
    slist = list(string)
    slist[i], slist[j] = slist[j], slist[i]
    return "".join(slist)


def calculate(n: str, count: int) -> str:
    length: int = len(n)
    que: set[str] = set([n])

    for _ in range(count):
        tmp: set[str] = set()

        while que:
            elem = que.pop()
            for i in range(length):
                for j in range(i + 1, length):
                    if i == 0 and elem[j] == "0":
                        continue
                    tmp.add(swap(elem, i, j))

        que = tmp

    return max(que) if que else "-1"


def main() -> None:
    n, k = input().split()

    print(calculate(n, int(k)))


if __name__ == "__main__":
    main()
