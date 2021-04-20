from collections import deque


def solution(s):
    answer = 0
    sdeque = deque()

    for ch in s:
        sdeque.append(ch)

    length = len(sdeque)
    count = 0
    while count < length:
        slist = []
        for ch in sdeque:
            if (len(slist) > 0
                    and ((slist[-1] == '[' and ch == ']')
                         or (slist[-1] == '{' and ch == '}')
                         or (slist[-1] == '(' and ch == ')'))):
                slist.pop()
            else:
                slist.append(ch)

        if len(slist) == 0:
            answer += 1

        sdeque.rotate(-1)
        count += 1

    return answer
