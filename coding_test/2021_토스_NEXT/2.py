from typing import Dict, List


def round_robin_sticky(servers: int, requests: List[int]) -> List[List[int]]:
    server: int = -1
    answer: List[List[int]] = [[] for _ in range(servers)]
    request_length: List[int] = [0 for _ in range(servers)]
    server_info: Dict[int, int] = {}
    for req in requests:
        if req in server_info:
            server = server_info[req]
        else:
            server = request_length.index(min(request_length))
            server_info[req] = server
            request_length[server] += requests.count(req)
        answer[server].append(req)
    return answer


def round_robin_not_sticky(servers: int, requests: List[int]) -> List[List[int]]:
    answer: List[List[int]] = [[] for _ in range(servers)]
    for index, req in enumerate(requests):
        answer[index % servers].append(req)
    return answer


def solution(servers: int, sticky: bool, requests: List[int]) -> List[List[int]]:
    if sticky:
        return round_robin_sticky(servers, requests)
    else:
        return round_robin_not_sticky(servers, requests)


print(solution(2, False, [1, 2, 3, 4]))
print(solution(2, True, [1, 1, 2, 2]))
print(solution(2, True, [1, 2, 2, 3, 4, 1]))
print(solution(2, True, [1, 2, 3, 1]))
