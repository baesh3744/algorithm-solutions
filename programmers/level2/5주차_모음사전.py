from bisect import bisect
from itertools import product
from typing import List


def solution(word: str):
    dictionary: List[str] = []
    for length in range(1, 6):
        dictionary.extend("".join(string) for string in product("AEIOU", repeat=length))
    dictionary.sort()
    return bisect(dictionary, word)


# 6
print(solution("AAAAE"))
# 10
print(solution("AAAE"))
# 1563
print(solution("I"))
# 1189
print(solution("EIO"))
