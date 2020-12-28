import fileinput


def main(inp):
    print("task1", task1(inp))
    print("task2", task2(inp))


def process(instruction):
    op, arg = instruction.split(" ")
    acc_diff = 0
    ins_diff = 1
    if op == "acc":
        acc_diff = int(arg)
    if op == "jmp":
        ins_diff = int(arg)
    return acc_diff, ins_diff


def task1(inp):
    accumulator = 0
    cur = 0
    already_executed = set()
    while cur not in already_executed:
        if cur >= len(inp):
            return accumulator, True
        already_executed.add(cur)
        acc_diff, ins_diff = process(inp[cur])
        accumulator += acc_diff
        cur += ins_diff
    return accumulator, False


def task2(inp):
    for i in range(len(inp)):
        if "jmp" not in inp[i] and "nop" not in inp[i]:
            continue
        inp_copy = inp[:]
        if "jmp" in inp[i]:
            inp_copy[i] = inp[i].replace("jmp", "nop")
        if "nop" in inp[i]:
            inp_copy[i] = inp[i].replace("nop", "jmp")
        res, normal = task1(inp_copy)
        if normal:
            return res


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
