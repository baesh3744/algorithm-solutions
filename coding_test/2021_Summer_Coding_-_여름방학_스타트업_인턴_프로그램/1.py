from typing import List


def solution(code: str, day: str, data: List[str]) -> List[int]:
    selected: List[str] = []
    splited_data: List[List[str]] = [text.split(' ') for text in data]

    for data_list in splited_data:
        price_data, code_data, time_data = [
            text.split('=')[1] for text in data_list]

        if code_data == code and time_data[:-2] == day:
            selected.append(time_data[-2:] + price_data)

    selected.sort(key=lambda x: x[:2])

    answer: List[int] = [int(text[2:]) for text in selected]
    return answer


print(solution("012345", "20190620",
               ["price=80 code=987654 time=2019062113", "price=90 code=012345 time=2019062014", "price=120 code=987654 time=2019062010", "price=110 code=012345 time=2019062009", "price=95 code=012345 time=2019062111"]))
