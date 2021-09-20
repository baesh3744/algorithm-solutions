import re


def solution(new_id: str) -> str:
    new_id = new_id.lower()
    new_id = re.sub(r"[^a-z0-9-_.]*", "", new_id)
    new_id = re.sub(r"\.{2,}", ".", new_id)
    new_id = re.sub(r"^\.|\.$", "", new_id)
    if not new_id:
        new_id = "aaa"
    new_id = new_id[:15]
    new_id = re.sub(r"\.$", "", new_id)
    if len(new_id) <= 2:
        new_id += new_id[-1] * (3 - len(new_id))
    return new_id


# "bat.y.abcdefghi"
print(solution("...!@BaT#*..y.abcdefghijklm"))
# "z--"
print(solution("z-+.^."))
# "aaa"
print(solution("=.="))
# "123_.def"
print(solution("123_.def"))
# "abcdefghijklmn"
print(solution("abcdefghijklmn.p"))
