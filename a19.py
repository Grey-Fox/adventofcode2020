import fileinput


def main(inp):
    print("task1", task1(inp))
    print("task2", task2(inp))


def parse_input(inp):
    rools = {}
    i = iter(inp)
    for row in i:
        if row == "":
            break
        key, rs = row.split(": ")
        rs = [[p.strip('"') for p in r.split(" ")] for r in rs.split(" | ")]
        rools[key] = rs

    messages = list(i)
    return rools, messages


def check(msg, rool, all_rools):
    def subcheck(msg, start, rool, depth):
        if depth > len(msg):
            return []
        if not rool:
            return [start]

        i = start
        p = rool[0]
        if not p.isdigit():
            if i < len(msg) and msg[i] == p:
                i += 1
                return subcheck(msg, i, rool[1:], depth + 1)
            else:
                return []

        new_indexes = []
        for r in all_rools[p]:
            t = subcheck(msg, i, r, depth + 1)
            if t:
                new_indexes.extend(t)

        res = []
        for i in new_indexes:
            t = subcheck(msg, i, rool[1:], depth + 1)
            if t:
                res.extend(t)
        return res

    ends = subcheck(msg, 0, rool[0], 0)
    return len(msg) in ends


def task1(inp):
    rools, messages = parse_input(inp)

    count = 0
    for msg in messages:
        if check(msg, rools["0"], rools):
            count += 1
    return count


def task2(inp):
    rools, messages = parse_input(inp)
    rools["8"] = [["42"], ["42", "8"]]
    rools["11"] = [["42", "31"], ["42", "11", "31"]]

    count = 0
    for msg in messages:
        if check(msg, rools["0"], rools):
            count += 1
    return count


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
