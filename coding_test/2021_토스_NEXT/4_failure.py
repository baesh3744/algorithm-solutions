from typing import List


def solution(input: str) -> str:
    command = input.split("\n")
    answer: str = ""
    start: int = 0

    for index, cmd in enumerate(command):
        firstRow = command[index].split()
        if (
            len(firstRow) != 2
            or not firstRow[0].isdigit()
            or not firstRow[1].isdigit()
            or not 0 < int(firstRow[0]) < 10000
            or not 0 < int(firstRow[1]) < 100000
        ):
            if len(answer) != 0:
                answer += "\n"
            answer += "ERROR"
        else:
            start = index

    m, n = map(int, command[start].split())
    if len(answer) != 0:
        answer += "\n"
    answer += command[start]
    cantShow: int = 0
    showInOneDay: int = 0
    showPrevDays: int = 0
    showCountList: List[int] = []
    for cmd in command[start + 1 :]:
        answer += "\n"
        if cmd == "SHOW":
            if cantShow == 0 and showPrevDays + showInOneDay < n:
                answer += "1"
                showInOneDay += 1
            else:
                answer += "0"
        elif cmd == "NEGATIVE":
            answer += "0"
            cantShow = m + 1
        elif cmd == "NEXT":
            answer += "-"
            showCountList.append(showInOneDay)
            showPrevDays = sum(showCountList[-1 * m :])
            if cantShow > 0:
                cantShow -= 1
            elif showPrevDays >= n:
                cantShow = m
            showInOneDay = 0
        elif cmd == "EXIT":
            answer += "BYE"
            break
        else:
            answer += "ERROR"
    return answer


# print(solution("1 2\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nEXIT"))
# print(solution("2 2\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nEXIT"))
# print(
#     solution(
#         "2 3\nSHOW\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nEXIT"
#     )
# )
# print(
#     solution(
#         "2 3\nSHOW\nNEGATIVE\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nNEXT\nSHOW\nSHOW\nNEXT\nSHOW\nSHOW\nEXIT"
#     )
# )
# print(solution("1 3\nSHOW\nHELLO\nEXIT"))
# print(solution("a 3\nNEXT"))
print(solution("a 3\n1 3"))
