import fileinput
from itertools import groupby
from functools import reduce


def main(inp):
    print("task1", task1(get_groups(inp)))
    print("task2", task2(get_groups(inp)))


def get_groups(inp):
    for k, lines in groupby(inp, key=lambda x: x == ""):
        if k:
            continue
        yield list(lines)


def task1(groups):
    count = 0
    for group in groups:
        count += len(set("".join(group)))
    return count


def task2(groups):
    count = 0
    for group in groups:
        count += len(reduce(lambda x, y: set(x) & set(y), group))
    return count


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
