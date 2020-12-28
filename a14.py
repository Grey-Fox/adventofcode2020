import fileinput
import re


def main(inp):
    print("task1", task1(inp))
    print("task2", task2(inp))


def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


def task1(prog):
    def apply_mask(value, mask):
        for i, v in enumerate(mask[::-1]):
            if v == "1":
                value = set_bit(value, i)
            elif v == "0":
                value = clear_bit(value, i)
        return value

    mem = {}
    mask = ""
    for row in prog:
        if row.startswith("mask = "):
            mask = row[7:]
        elif row.startswith("mem"):
            addr, value = re.match(r"mem\[(\d+)\] = (\d+)", row).groups()
            addr = int(addr)
            value = int(value)
            mem[addr] = apply_mask(value, mask)

    return sum(mem.values())


def task2(prog):
    def apply_mask(addr, mask):
        for i, v in enumerate(mask[::-1]):
            if v == "1":
                addr = set_bit(addr, i)
        addrs = {addr}
        for i, v in enumerate(mask[::-1]):
            if v == "X":
                for a in list(addrs):
                    addrs.add(set_bit(a, i))
                    addrs.add(clear_bit(a, i))
        return list(addrs)

    mem = {}
    mask = ""
    for row in prog:
        if row.startswith("mask = "):
            mask = row[7:]
        elif row.startswith("mem"):
            addr, value = re.match(r"mem\[(\d+)\] = (\d+)", row).groups()
            addr = int(addr)
            value = int(value)
            for a in apply_mask(addr, mask):
                mem[a] = value

    return sum(mem.values())


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
