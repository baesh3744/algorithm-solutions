from typing import Dict, List


ENTER = "Enter"
LEAVE = "Leave"


def get_final_names(splitted_record: List[List[str]]) -> Dict[str, str]:
    names: Dict[str, str] = {}

    for cmd, *rest in splitted_record:
        if cmd == LEAVE:
            continue

        uid, name = rest
        names[uid] = name

    return names


def solution(record: List[str]) -> List[str]:
    splitted_record: List[List[str]] = [rec.split() for rec in record]
    names = get_final_names(splitted_record)

    answer: List[str] = []
    for cmd, *rest in splitted_record:
        uid = rest[0]
        if cmd == ENTER:
            answer.append(f"{names[uid]}님이 들어왔습니다.")
        elif cmd == LEAVE:
            answer.append(f"{names[uid]}님이 나갔습니다.")

    return answer


# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
print(
    solution(
        [
            "Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan",
        ]
    )
)
