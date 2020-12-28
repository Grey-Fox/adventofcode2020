import fileinput
import re
from collections import defaultdict


def main(inp):
    print("task1", task1(inp))
    print("task2", task2(inp))


def parse_ticket(t):
    return [int(i) for i in t.split(",")]


def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


def parse_notes(notes):
    g = iter(notes)
    rools = {}
    for row in g:
        if not row:
            break
        rool = re.match(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", row).groups()
        rools[rool[0]] = split_list([int(i) for i in rool[1:]])
    next(g)
    your_ticket = parse_ticket(next(g))
    next(g)
    next(g)
    nearby_tickets = []
    for t in g:
        nearby_tickets.append(parse_ticket(t))
    return rools, your_ticket, nearby_tickets


def task1(notes):
    rools, _, nearby_tickets = parse_notes(notes)
    s = 0
    for t in nearby_tickets:
        for v in t:
            if not any(any(b1 <= v <= b2 for b1, b2 in r) for r in rools.values()):
                s += v
    return s


def task2(notes):
    rools, your_ticket, nearby_tickets = parse_notes(notes)
    invalid_tickets = set([])
    for i, t in enumerate(nearby_tickets):
        for v in t:
            if not any(any(b1 <= v <= b2 for b1, b2 in r) for r in rools.values()):
                invalid_tickets.add(i)

    col2rools = defaultdict(set)
    for col in range(len(nearby_tickets[0])):
        for name, rool in rools.items():
            good = True
            for i, tiket in enumerate(nearby_tickets):
                if i in invalid_tickets:
                    continue
                v = tiket[col]
                if not any(b1 <= tiket[col] <= b2 for b1, b2 in rool):
                    good = False
                    break
            if good:
                col2rools[col].add(name)

    rool2col = {}
    while len(rool2col) != len(rools):
        detected_rool = None
        detected_col = None
        for col, rs in col2rools.items():
            if col in rool2col.values():
                continue
            if len(rs) == 1:
                detected_rool = rs.pop()
                detected_col = col
                break
        else:
            raise Exception("shit happens")
        for col in col2rools:
            col2rools[col].discard(detected_rool)
        rool2col[detected_rool] = detected_col

    res = 1
    for name, col in rool2col.items():
        if name.startswith("departure"):
            res *= your_ticket[col]
    return res


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
