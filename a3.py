def main():
    f = open("a3_input")

    lines = f.readlines()
    tree_map = [r.strip() for r in lines]
    print("task 1:", task1(tree_map))
    print("task 2:", task2(tree_map))


def task1(tree_map, dx=3, dy=1):
    x = 0
    y = 0
    count_tree = 0
    for i, line in enumerate(tree_map):
        if i != y:
            continue
        if line[x % len(line)] == "#":
            count_tree += 1
        x += dx
        y += dy
    return count_tree


def task2(tree_map):
    res = 1
    for s in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        res *= task1(tree_map, *s)
    return res


if __name__ == "__main__":
    main()
