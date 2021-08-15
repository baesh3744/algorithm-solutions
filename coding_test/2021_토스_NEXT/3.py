def solution(amountText: str):
    hasComma: bool = False
    if len(amountText) > 3 and amountText[-4] == ",":
        hasComma = True

    if (len(amountText) != 1 and amountText[0] == "0") or amountText[0] == ",":
        return False

    for index, ch in enumerate(reversed(amountText)):
        if index % 4 == 3 and hasComma:
            if ch != ",":
                return False
        elif not ch.isdigit():
            return False
    return True


print(solution("1만원"))
print(solution("10,000원"))
print(solution("+300"))
print(solution("0100"))
print(solution("25,000,123"))  # True
print(solution("24,999,99"))
print(solution("10,000,"))
print(solution(",999,000"))
