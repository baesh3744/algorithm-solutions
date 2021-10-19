from typing import List, Tuple


def solution(n: int, k: int, cmd: List[str]):
    removed: List[Tuple[int, int, int]] = []
    table = {idx: [idx - 1, idx + 1] for idx in range(n)}
    answer = ["O" for _ in range(n)]

    for command in cmd:
        if command == "Z":
            idx, prev, next = removed.pop()
            answer[idx] = "O"
            if prev != -1:
                table[prev][1] = idx
            if next != n:
                table[next][0] = idx
        elif command == "C":
            prev, next = table[k]
            removed.append((k, prev, next))
            answer[k] = "X"
            k = next if next != n else prev
            if prev != -1:
                table[prev][1] = next
            if next != n:
                table[next][0] = prev
        else:
            next = 0 if command[0] == "U" else 1
            for _ in range(int(command.split()[1])):
                k = table[k][next]

    return "".join(answer)


# "OOOOXOOO"
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
# "OOXOXOOO"
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
