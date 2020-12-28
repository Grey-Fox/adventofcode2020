import fileinput
from collections import defaultdict


def main(inp):
    print("task1", task1(inp))
    print("task2", task2(inp))


def apply_rools(tiles, inp):
    for row in inp:
        steps = iter(row)
        x, y = 0, 0
        for step in steps:
            if step in ("n", "s"):
                step += next(steps)
            if step == "e":
                x += 2
            elif step == "se":
                x += 1
                y -= 1
            elif step == "sw":
                x -= 1
                y -= 1
            elif step == "w":
                x -= 2
            elif step == "nw":
                x -= 1
                y += 1
            elif step == "ne":
                x += 1
                y += 1
        if tiles[x, y] == "white":
            tiles[x, y] = "black"
        else:
            tiles[x, y] = "white"


def task1(inp):
    tiles = defaultdict(lambda: "white")
    apply_rools(tiles, inp)
    return list(tiles.values()).count("black")


def get_arround(x, y):
    return [
        (x + 2, y),
        (x + 1, y - 1),
        (x - 1, y - 1),
        (x - 2, y),
        (x - 1, y + 1),
        (x + 1, y + 1),
    ]


def apply_rools_2(tiles):
    new_tiles = tiles.copy()
    white_to_check = set()
    for (x, y), color in list(tiles.items()):
        if tiles[x, y] == "white":
            continue
        black_count = 0
        for x1, y1 in get_arround(x, y):
            if tiles[x1, y1] == "white":
                white_to_check.add((x1, y1))
            else:
                black_count += 1
        if black_count == 0 or black_count > 2:
            new_tiles[x, y] = "white"

    for (x, y) in white_to_check:
        black_count = 0
        for x1, y1 in get_arround(x, y):
            if tiles[x1, y1] == "black":
                black_count += 1
        if black_count == 2:
            new_tiles[x, y] = "black"

    return new_tiles


def task2(inp):
    tiles = defaultdict(lambda: "white")
    apply_rools(tiles, inp)
    for _ in range(100):
        tiles = apply_rools_2(tiles)
    return list(tiles.values()).count("black")


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
