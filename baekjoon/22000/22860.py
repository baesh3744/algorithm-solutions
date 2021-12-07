import sys
from collections import defaultdict


input = sys.stdin.readline


class Directory:
    def __init__(self) -> None:
        self.subdirs: list[str] = []
        self.files: set[str] = set()
        self.cnt_file = 0


class Structure:
    def __init__(self) -> None:
        self.structure: defaultdict[str, Directory] = defaultdict(Directory)
        self.counts: dict[str, tuple[int, int]] = dict()

    def add_directory(self, parent: str, dir: str) -> None:
        self.structure[parent].subdirs.append(dir)

    def add_file(self, parent: str, file: str) -> None:
        self.structure[parent].cnt_file += 1
        self.structure[parent].files.add(file)

    def count(self, dir: str) -> tuple[set[str], int]:
        files: set[str] = self.structure[dir].files
        cnt_file: int = self.structure[dir].cnt_file

        for subdir in self.structure[dir].subdirs:
            subfiles, subcnt = self.count(subdir)
            files.update(subfiles)
            cnt_file += subcnt

        self.counts[dir] = (len(files), cnt_file)
        return files, cnt_file


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    n, m = map(int, input().split())

    st: Structure = Structure()
    for _ in range(n + m):
        p, f, c = input().split()
        if c == "1":
            st.add_directory(p, f)
        else:
            st.add_file(p, f)

    st.count("main")

    q = int(input())
    for _ in range(q):
        query = input().strip().split("/")
        print(*st.counts[query[-1]])
