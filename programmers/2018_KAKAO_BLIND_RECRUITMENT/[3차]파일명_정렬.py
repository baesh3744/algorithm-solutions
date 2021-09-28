from typing import List, Tuple


def split(file: str) -> Tuple[str, str]:
    hend_idx, nend_idx = -1, len(file)
    is_met_digit: bool = False
    for idx, char in enumerate(file):
        if char.isdigit():
            if not is_met_digit:
                hend_idx = idx
            is_met_digit = True
        elif is_met_digit:
            nend_idx = idx
            break
    return file[:hend_idx], file[hend_idx:nend_idx]


def solution(files: List[str]) -> List[str]:
    parsed: List[Tuple[str, int, int]] = []
    for idx, file in enumerate(files):
        head, number = split(file)
        parsed.append((head.lower(), int(number), idx))
    parsed.sort()
    return [files[idx] for _, _, idx in parsed]


#  ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
print(
    solution(
        ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    )
)
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]
print(
    solution(
        [
            "F-5 Freedom Fighter",
            "B-50 Superfortress",
            "A-10 Thunderbolt II",
            "F-14 Tomcat",
        ]
    )
)
# ["img01"]
print(solution(["img01"]))
