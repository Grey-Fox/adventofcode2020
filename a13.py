import fileinput
from math import ceil


def main(inp):
    print("task1", task1(inp))
    print("task2", task2(inp))


def task1(notes):
    if not notes[0].isdigit():
        return
    ts = int(notes[0])
    ids = [int(n) for n in notes[1].split(",") if n != "x"]
    wait = max(ids)
    bus = 0
    for n in ids:
        tmp = int(ceil(ts / n)) * n - ts
        if tmp < wait:
            wait = tmp
            bus = n
    return bus * wait


def task2(notes):
    ids = [int(n.replace("x", "0")) for n in notes[-1].split(",")]
    step = ids[0]
    ts = ids[0]
    for i in range(1, len(ids)):
        if ids[i] == 0:
            continue
        while ts % ids[i] != ids[i] - i % ids[i]:
            ts += step
        step *= ids[i]
    return ts


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
