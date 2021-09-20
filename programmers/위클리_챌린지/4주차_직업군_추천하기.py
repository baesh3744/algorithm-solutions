from typing import List


def index_of(string_list: List[str], target: str) -> int:
    try:
        return string_list.index(target)
    except ValueError:
        return -1


def solution(table: List[str], languages: List[str], preference: List[int]) -> str:
    answer: str = ""
    max_score: int = -1

    for string in table:
        job_score_list: List[str] = list(reversed(string.split()))
        job_score_list, job = job_score_list[:-1], job_score_list[-1]

        score: int = 0
        for language, prf in zip(languages, preference):
            score += prf * (index_of(job_score_list, language) + 1)

        if score == max_score:
            answer = min(answer, job)
        elif score > max_score:
            max_score = score
            answer = job

    return answer


# "HARDWARE"
print(
    solution(
        [
            "SI JAVA JAVASCRIPT SQL PYTHON C#",
            "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
            "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
            "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
            "GAME C++ C# JAVASCRIPT C JAVA",
        ],
        ["PYTHON", "C++", "SQL"],
        [7, 5, 5],
    )
)
# "PORTAL"
print(
    solution(
        [
            "SI JAVA JAVASCRIPT SQL PYTHON C#",
            "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
            "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
            "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
            "GAME C++ C# JAVASCRIPT C JAVA",
        ],
        ["JAVA", "JAVASCRIPT"],
        [7, 5],
    )
)
# "CONTENTS"
print(
    solution(
        [
            "SI JAVA JAVASCRIPT SQL PYTHON C#",
            "CONTENTS JAVA JAVASCRIPT SQL PYTHON C#",
            "HARDWARE JAVA JAVASCRIPT SQL PYTHON C#",
            "PORTAL JAVA JAVASCRIPT SQL PYTHON C#",
            "GAME JAVA JAVASCRIPT SQL PYTHON C#",
        ],
        ["JAVA", "JAVASCRIPT"],
        [7, 5],
    )
)
