import fileinput
from itertools import combinations

PREV_LEN = 25


def main(inp):
    print("task1", task1(to_int(inp)))
    print("task2", task2(list(to_int(inp))))


def to_int(inp):
    for i in inp:
        yield int(i)


def check_is_sum(n, prev):
    for x, y in combinations(prev, 2):
        if x + y == n:
            return True
    return False


def task1(numbers):
    prev = []
    for n in numbers:
        if len(prev) >= PREV_LEN:
            if not check_is_sum(n, prev):
                return n
        prev.append(n)
        prev = prev[-PREV_LEN:]


def task2(numbers):
    n = task1(numbers)
    i = 0
    j = 2
    while True:
        s = sum(numbers[i:j])

        if s == n:
            break

        if s < n:
            j = j + 1

        if s > n or j > len(numbers):
            i = i + 1
            j = i + 2

        if i >= len(numbers):
            return None

    return min(numbers[i:j]) + max(numbers[i:j])


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
