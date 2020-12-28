import fileinput


def main(inp):
    print("task1", task1(inp))
    print("task2", task2(inp))


def calc(subj, loop):
    res = 1
    for _ in range(loop):
        res = res * subj % 20201227
    return res


def crack(subj, pk):
    res = 1
    loop = 0
    while True:
        loop += 1
        res = res * subj % 20201227
        if res == pk:
            return loop


def task1(inp):

    card_pk = int(inp[0])
    door_pk = int(inp[1])
    card_loop = crack(7, card_pk)
    return calc(door_pk, card_loop)


def task2(inp):
    pass


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
