import fileinput
from collections import defaultdict


def main(inp):
    print("task1", task1(list(to_int(inp))))
    print("task2", task2(list(to_int(inp))))


def to_int(inp):
    for i in inp:
        yield int(i)


def task1(adapters):
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()
    d = defaultdict(int)
    for i in range(1, len(adapters)):
        d[adapters[i] - adapters[i - 1]] += 1
    return d[1] * d[3]


def task2(adapters):
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()

    def get_count(last, ind, end):
        if ind >= end - 1:
            return 1
        c = get_count(ind, ind + 1, end)
        if adapters[ind + 1] - adapters[last] <= 3:
            c += get_count(last, ind + 1, end)
        return c

    res = 1
    last = 0
    for i in range(1, len(adapters)):
        if adapters[i] - adapters[i - 1] == 3:
            res *= get_count(last, last + 1, i)
            last = i

    return res


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
