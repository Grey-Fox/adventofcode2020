import fileinput
from collections import defaultdict


def main(inp):
    print("task1", task1(get_cube(inp)))
    print("task2", task2(get_hcube(inp)))


def get_cube(inp):
    cube = defaultdict(lambda: ".")
    for i, row in enumerate(inp):
        for j, s in enumerate(row):
            cube[(i, j, 0)] = s
    return cube


def get_hcube(inp):
    cube = defaultdict(lambda: ".")
    for i, row in enumerate(inp):
        for j, s in enumerate(row):
            cube[(i, j, 0, 0)] = s
    return cube


def get_count_of_active(cube, x, y, z):
    c = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == 0 and j == 0 and k == 0:
                    continue
                if cube[x + i, y + j, z + k] == "#":
                    c += 1
    return c


def get_count_of_active_h(cube, x, y, z, w):
    c = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for m in range(-1, 2):
                    if i == 0 and j == 0 and k == 0 and m == 0:
                        continue
                    if cube[x + i, y + j, z + k, w + m] == "#":
                        c += 1
    return c


def print_cube(cube):
    xmin = min(cube, key=lambda d: d[0])[0]
    ymin = min(cube, key=lambda d: d[1])[1]
    zmin = min(cube, key=lambda d: d[2])[2]
    xmax = max(cube, key=lambda d: d[0])[0]
    ymax = max(cube, key=lambda d: d[1])[1]
    zmax = max(cube, key=lambda d: d[2])[2]
    print(">" * 40)
    for z in range(zmin, zmax + 1):
        print("z = ", z)
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                print(cube[x, y, z], end="")
            print()
    print("<" * 40)


def task1(cube):
    for _ in range(6):
        xmin = min(cube, key=lambda d: d[0])[0] - 1
        ymin = min(cube, key=lambda d: d[1])[1] - 1
        zmin = min(cube, key=lambda d: d[2])[2] - 1
        xmax = max(cube, key=lambda d: d[0])[0] + 1
        ymax = max(cube, key=lambda d: d[1])[1] + 1
        zmax = max(cube, key=lambda d: d[2])[2] + 1
        new_cube = cube.copy()
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                for z in range(zmin, zmax + 1):
                    c = get_count_of_active(cube, x, y, z)
                    if cube[x, y, z] == "#":
                        if c not in (2, 3):
                            new_cube[x, y, z] = "."
                    else:
                        if c == 3:
                            new_cube[x, y, z] = "#"
        cube = new_cube
    return sum(1 if i == "#" else 0 for i in cube.values())


def task2(hcube):
    for _ in range(6):
        xmin = min(hcube, key=lambda d: d[0])[0] - 1
        ymin = min(hcube, key=lambda d: d[1])[1] - 1
        zmin = min(hcube, key=lambda d: d[2])[2] - 1
        wmin = min(hcube, key=lambda d: d[3])[3] - 1
        xmax = max(hcube, key=lambda d: d[0])[0] + 1
        ymax = max(hcube, key=lambda d: d[1])[1] + 1
        zmax = max(hcube, key=lambda d: d[2])[2] + 1
        wmax = max(hcube, key=lambda d: d[3])[3] + 1
        new_hcube = hcube.copy()
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                for z in range(zmin, zmax + 1):
                    for w in range(wmin, wmax + 1):
                        c = get_count_of_active_h(hcube, x, y, z, w)
                        if hcube[x, y, z, w] == "#":
                            if c not in (2, 3):
                                new_hcube[x, y, z, w] = "."
                        else:
                            if c == 3:
                                new_hcube[x, y, z, w] = "#"
        hcube = new_hcube
    return sum(1 if i == "#" else 0 for i in hcube.values())


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
