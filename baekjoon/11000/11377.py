import sys


input = sys.stdin.readline


def match(emp: int) -> bool:
    visited[emp] = True
    for work in cando_list[emp if emp < n else emp - n]:
        origin_emp: int = works[work]
        if origin_emp == -1 or (not visited[origin_emp] and match(origin_emp)):
            employees[emp] = work
            works[work] = emp
            return True
    return False


def main() -> None:
    global n, cando_list, employees, works, visited
    n, m, k = map(int, input().split())
    cando_list = [
        list(map(lambda x: int(x) - 1, input().split()[1:])) for _ in range(n)
    ]

    cnt: int = 0
    employees = [-1 for _ in range(2 * n)]
    works = [-1 for _ in range(m)]
    for emp, work in enumerate(employees):
        if k == 0:
            break
        if work == -1:
            visited = [False for _ in range(2 * n)]
            if match(emp):
                cnt += 1
                if emp >= n:
                    k -= 1
    print(cnt)


if __name__ == "__main__":
    main()
