import fileinput


def main(inp):
    print("task1", task1(to_int(inp[-1])))
    print("task2", task2(to_int(inp[-1])))


def to_int(s):
    return [int(i) for i in s.split(",")]


def get_res(nums, spoken):
    m = {}
    for i, n in enumerate(nums[:-1]):
        m[n] = i + 1

    i = len(nums)
    nxt = nums[-1]
    while True:
        if i >= spoken:
            break
        if nxt in m:
            m[nxt], nxt = i, i - m[nxt]
        else:
            m[nxt], nxt = i, 0
        i += 1

    return nxt


def task1(nums):
    return get_res(nums, 2020)


def task2(nums):
    return get_res(nums, 30000000)


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
