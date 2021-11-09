def bfs() -> int:
    time: int = 0
    que: set[tuple[int, int]] = set()

    que.add((1, 0))

    while True:
        new_que: set[tuple[int, int]] = set()

        for screen, clip in que:
            if screen == s:
                return time
            new_que.add((screen, screen))
            if clip > 0:
                new_que.add((screen + clip, clip))
            if screen > 0:
                new_que.add((screen - 1, clip))

        time += 1
        que = new_que


if __name__ == "__main__":
    s = int(input())

    print(bfs())
