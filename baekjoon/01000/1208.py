from collections import deque


left_dict: dict[int, int] = {}


def dfs_left(s: int, half_size: int, nums: list[int]) -> int:
    cnt: int = 0
    que: deque[tuple[int, int]] = deque([(0, 0)])

    while que:
        sum, idx = que.popleft()

        if idx == half_size:
            continue

        # idx번째 숫자를 선택하지 않는 경우
        que.append((sum, idx + 1))

        # idx번째 숫자를 선택하는 경우
        sum += nums[idx]
        if sum in left_dict:
            left_dict[sum] += 1
        else:
            left_dict[sum] = 1
        que.append((sum, idx + 1))

    # 왼쪽 수열에서만 만들기
    if s in left_dict:
        cnt += left_dict[s]

    return cnt


def dfs_right(s: int, half_size: int, nums: list[int]) -> int:
    cnt: int = 0
    que: deque[tuple[int, int]] = deque([(0, half_size)])

    while que:
        sum, idx = que.popleft()

        if idx == len(nums):
            continue

        # idx번째 숫자를 선택하지 않는 경우
        que.append((sum, idx + 1))

        # idx번째 숫자를 선택하는 경우
        sum += nums[idx]
        if s - sum in left_dict:  # 왼쪽 수열과 오른쪽 수열을 합쳐 만들기
            cnt += left_dict[s - sum]
        if sum == s:  # 오른쪽 수열에서만 만들기
            cnt += 1
        que.append((sum, idx + 1))

    return cnt


def main() -> None:
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))

    half_size: int = n // 2
    cnt: int = 0
    cnt += dfs_left(s, half_size, nums)
    cnt += dfs_right(s, half_size, nums)
    print(cnt)


if __name__ == "__main__":
    main()
