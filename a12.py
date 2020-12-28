import fileinput
from math import pi, cos, sin


def main(inp):
    print("task1", task1(inp))
    print("task2", task2(inp))


def task1(commands):
    x = y = 0
    d = (1, 0)
    for command in commands:
        c, val = command[0], int(command[1:])
        if c == "N":
            y += val
        elif c == "S":
            y -= val
        elif c == "E":
            x += val
        elif c == "W":
            x -= val
        elif c == "L":
            assert val in list(range(0, 361, 90))
            a = val * pi / 180
            d = (
                int(round(cos(a) * d[0] - sin(a) * d[1])),
                int(round(sin(a) * d[0] + cos(a) * d[1])),
            )
        elif c == "R":
            assert val in list(range(0, 361, 90))
            a = -val * pi / 180
            d = (
                int(cos(a) * d[0] - sin(a) * d[1]),
                int(sin(a) * d[0] + cos(a) * d[1]),
            )
        elif c == "F":
            x += d[0] * val
            y += d[1] * val
    return abs(x) + abs(y)


def task2(commands):
    x = y = 0
    xp = 10
    yp = 1
    for command in commands:
        c, val = command[0], int(command[1:])
        if c == "N":
            yp += val
        elif c == "S":
            yp -= val
        elif c == "E":
            xp += val
        elif c == "W":
            xp -= val
        elif c == "L":
            assert val in list(range(0, 361, 90))
            a = val * pi / 180
            xp, yp = (
                int(round(cos(a) * xp - sin(a) * yp)),
                int(round(sin(a) * xp + cos(a) * yp)),
            )
        elif c == "R":
            assert val in list(range(0, 361, 90))
            a = -val * pi / 180
            xp, yp = (
                int(round(cos(a) * xp - sin(a) * yp)),
                int(round(sin(a) * xp + cos(a) * yp)),
            )
        elif c == "F":
            x += xp * val
            y += yp * val
    return abs(x) + abs(y)


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
