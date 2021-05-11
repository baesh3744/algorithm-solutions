from typing import Dict, List, Tuple


def solution(s: str) -> List[int]:
    for char in ['{', '}']:
        s = s.replace(char, '')

    dict: Dict[int, int] = {}
    for num in s.split(','):
        if (num := int(num)) in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    sorted_dict: List[Tuple[int, int]] = sorted(
        dict.items(), key=(lambda x: x[1]), reverse=True)

    return list(map(lambda x: x[0], sorted_dict))


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))               # [111, 20]
print(solution("{{123}}"))                        # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))  # [3, 2, 4, 1]
