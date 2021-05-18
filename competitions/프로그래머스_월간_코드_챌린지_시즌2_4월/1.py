def solution(absolutes, signs):
    answer = 0

    for value, sign in zip(absolutes, signs):
        sign = 1 if sign else -1
        answer += sign * value

    return answer
