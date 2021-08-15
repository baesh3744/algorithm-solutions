import math


def solution(orderAmount: int, taxFreeAmount: int, serviceFee: int):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료
    # 주문금액 - 봉사료 - 비과세 = 과세 + 부가가치세
    amount: int = orderAmount - serviceFee - taxFreeAmount
    if amount == 1:
        answer = 0
    else:
        answer = math.ceil(amount / 11)
    return answer
