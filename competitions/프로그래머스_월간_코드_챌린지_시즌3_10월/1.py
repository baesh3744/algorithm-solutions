def solution(n: int) -> int:
    answer = 1
    for num in range(2, n):
        if n % num == 1:
            answer = num
            break
    return answer

# 3
print(solution(10))
# 11
print(solution(12))
