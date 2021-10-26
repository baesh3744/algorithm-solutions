import sys


input = sys.stdin.readline


def match(employee: int) -> bool:
    visited[employee] = True
    for work in doable_works[employee]:
        origin_employee: int = work_employee_list[work]
        if origin_employee == -1 or (
            not visited[origin_employee] and match(origin_employee)
        ):
            employee_work_list[employee] = work
            work_employee_list[work] = employee
            return True
    return False


def main() -> None:
    global doable_works, employee_work_list, work_employee_list, visited
    n, m = map(int, input().split())
    doable_works = [
        list(map(lambda x: int(x) - 1, input().split()[1:])) for _ in range(n)
    ]

    cnt: int = 0
    employee_work_list = [-1 for _ in range(n)]
    work_employee_list = [-1 for _ in range(m)]
    for employee, work in enumerate(employee_work_list):
        if work == -1:
            visited = [False for _ in range(n)]
            if match(employee):
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
