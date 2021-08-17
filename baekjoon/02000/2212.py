def main() -> None:
    _ = int(input())
    k = int(input())
    sensor_list = list(set(map(int, input().split())))

    sensor_list.sort()
    diff_list = [
        sensor_list[index + 1] - value for index, value in enumerate(sensor_list[:-1])
    ]
    diff_list.sort()
    print(sum(diff_list[: len(diff_list) + 1 - k]))


if __name__ == "__main__":
    main()
