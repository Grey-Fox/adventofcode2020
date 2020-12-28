import fileinput


def main(inp):
    print("task1", task1(inp))
    print("task2", task2(inp))


def to_bin(seat):
    return seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")


def get_id(bseat):
    return int(bseat, 2)


def task1(seats):
    return max(get_id(to_bin(s)) for s in seats)


def task2(seats):
    ids = [get_id(to_bin(s)) for s in seats]
    ids.sort()
    for i in range(len(ids) - 1):
        if ids[i + 1] - ids[i] == 2:
            return ids[i] + 1


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
