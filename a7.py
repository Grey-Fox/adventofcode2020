import fileinput
import re


def main(inp):
    print("task1", task1(get_rools(inp)))
    print("task2", task2(get_rools(inp)))


def get_rools(inp):
    rools = {}
    for row in inp:
        color, content = re.match(r"^(.*) bags contain (.*)\.$", row).groups()
        rools[color] = {}
        if content.startswith("no other"):
            continue
        for r in content.split(", "):
            n, col1, col2, *_ = r.split(" ")
            rools[color]["{} {}".format(col1, col2)] = int(n)
    return rools


def task1(rools):
    res = {"shiny gold"}
    pl = 0
    while len(res) != pl:
        pl = len(res)
        for color, rool in rools.items():
            if set(rool) & res:
                res.add(color)
    return len(res) - 1


def task2(rools):
    def f(color):
        c = 0
        for new_color, num in rools[color].items():
            c += num + num * f(new_color)
        return c

    return f("shiny gold")


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
