import fileinput


def main(inp):
    print("task1", task1(get_seats(inp)))
    print("task2", task2(get_seats(inp)))


def get_seats(inp):
    seats = {}
    for i, row in enumerate(inp):
        for j, s in enumerate(row):
            seats[(i, j)] = s
    return seats


def get_count_of_occupied(seats, x, y):
    c = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0) and seats.get((x + i, y + j)) == "#":
                c += 1
    return c


def get_count_of_occupied2(seats, x, y):
    c = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            xc = x
            yc = y
            while True:
                xc = xc + i
                yc = yc + j
                if seats.get((xc, yc)) == ".":
                    continue
                if seats.get((xc, yc)) == "#":
                    c += 1
                break
    return c


def print_seats(seats):
    x, y = max(seats)
    for i in range(x + 1):
        for j in range(y + 1):
            print(seats[i, j], end="")
        print()


def task1(seats):
    while True:
        new_seats = seats.copy()
        for coord in new_seats:
            if new_seats[coord] == ".":
                continue
            count_of_occupied = get_count_of_occupied(seats, *coord)
            if new_seats[coord] == "#":
                if count_of_occupied >= 4:
                    new_seats[coord] = "L"
            else:
                if count_of_occupied == 0:
                    new_seats[coord] = "#"
        if seats == new_seats:
            break
        seats = new_seats

    return list(seats.values()).count("#")


def task2(seats):
    while True:
        new_seats = seats.copy()
        for coord in new_seats:
            if new_seats[coord] == ".":
                continue
            count_of_occupied = get_count_of_occupied2(seats, *coord)
            if new_seats[coord] == "#":
                if count_of_occupied >= 5:
                    new_seats[coord] = "L"
            else:
                if count_of_occupied == 0:
                    new_seats[coord] = "#"
        if seats == new_seats:
            break
        seats = new_seats

    return list(seats.values()).count("#")


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
