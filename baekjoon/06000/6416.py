from collections import Counter


def is_tree(end_list: list[int], cnt_node: int) -> bool:
    counter_length = len(Counter(end_list).most_common())
    return len(end_list) == counter_length and cnt_node == counter_length + 1


def main() -> None:
    k: int = 0

    while True:
        k += 1

        end_list: list[int] = []
        node_set: set[int] = set()

        while True:
            input_list = list(map(int, input().split()))

            if not input_list:
                continue

            if input_list[0] == -1:
                return

            end_list.extend(input_list[1::2])
            node_set.update(input_list)

            if input_list[-1] == 0:
                if len(end_list) == 1 or is_tree(end_list[:-1], len(node_set) - 1):
                    print("Case %d is a tree." % k)
                else:
                    print("Case %d is not a tree." % k)
                break


if __name__ == "__main__":
    main()
