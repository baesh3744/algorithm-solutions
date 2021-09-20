from itertools import product
from typing import List


def is_matched(uid: str, bid: str) -> bool:
    if len(uid) != len(bid):
        return False

    for idx in range(len(uid)):
        if uid[idx] != bid[idx] and bid[idx] != '*':
            return False

    return True


def solution(user_id: List[str], banned_id: List[str]):
    ban_length: int = len(banned_id)
    banned_index: List[List[int]] = [[] for _ in range(ban_length)]

    for bidx in range(ban_length):
        for uidx in range(len(user_id)):
            if is_matched(user_id[uidx], banned_id[bidx]):
                banned_index[bidx].append(uidx)

    banned_list: List[frozenset[int]] = []
    for banned_product in product(*banned_index):
        banned: frozenset[int] = frozenset(banned_product)
        if len(banned) == ban_length:
            banned_list.append(banned)

    return len(set(banned_list))


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
               ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
               ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
               ["fr*d*", "*rodo", "******", "******"]))
print(solution(['abcdefgh', 'bcdefgha', 'cdefghab', 'defghabc', 'efghabcd', 'fghabcde', 'ghabcdef', 'habcdefg'],
               ['********', '********', '********', '********', '********', '********', '********', '********']))
