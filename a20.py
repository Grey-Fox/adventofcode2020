import fileinput
from itertools import groupby
from math import sqrt

TILE_DIM = 10

MONSTER_DATA = (
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
)
MONSTER_X_LEN = 3
MONSTER_Y_LEN = 20


def main(inp):
    print("task1", task1(parse_input(inp)))
    print("task2", task2(parse_input(inp)))


class Image:
    def __init__(self, data):
        self.data = tuple(data)

    def __getitem__(self, coord):
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise Exception("bad coord")

        x, y = coord
        if isinstance(x, slice) and isinstance(y, slice):
            data = []
            for row in self.data[x]:
                data.append(row[y])
            return Image(data)
        if isinstance(y, slice):
            return self.data[x]
        if isinstance(x, slice):
            return "".join(r[y] for r in self.data)
        return self.data[x][y]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return iter(self.len)

    def rotate(self):
        new_data = []
        for i in range(len(self.data)):
            new_data.append(self[:, i][::-1])
        self.data = tuple(new_data)

    def xflip(self):
        new_data = []
        for row in self.data[::-1]:
            new_data.append(row)
        self.data = tuple(new_data)

    def yflip(self):
        new_data = []
        for row in self.data:
            new_data.append(row[::-1])
        self.data = tuple(new_data)

    def compare(self, other):
        if not self.data and not other.data:
            return True

        sd = self.data
        od = other.data
        if len(sd) != len(od):
            return False
        if len(sd[0]) != len(od[0]):
            return False
        for i in range(len(sd)):
            for j in range(len(sd[0])):
                if sd[i][j] != " " and od[i][j] != " " and sd[i][j] != od[i][j]:
                    return False
        return True

    def __str__(self):
        return "\n".join(self.data)


class Tile(Image):
    def __init__(self, id_, data):
        self.id = id_
        super().__init__(data)


def parse_input(inp):
    tiles = []
    for is_delim, tile in groupby(inp, lambda x: x == ""):
        if is_delim:
            continue
        header, *data = tile
        id_ = int(header.strip(":").split(" ")[1])
        tiles.append(Tile(id_, data))
    return tiles


MONSTER = Image(MONSTER_DATA)


def get_borders(tile):
    borders = []
    for i in (0, -1):
        borders.append(tile[i, :])
        borders.append(tile[:, i])
    return borders


def get_all_borders_vars(tile):
    borders = get_borders(tile)
    for b in borders[:]:
        borders.append(b[::-1])
    return borders


def find_corner(tiles):
    for tile in tiles:
        for i in range(4):
            top = tile[0, :]
            left = tile[:, 0]
            match = False
            for tile2 in tiles:
                if tile2.id == tile.id:
                    continue
                border_vars = get_all_borders_vars(tile2)
                if top in border_vars or left in border_vars:
                    match = True
                    break
            if not match:
                return tile
            tile.rotate()
    raise Exception("corner not found")


def find_tile_with_same_edge(edge, tiles, key=lambda t: t[:, 0]):
    for tile in tiles:
        for f in range(3):
            for _ in range(4):
                if edge == key(tile):
                    return tile
                tile.rotate()
            if f == 0:
                tile.xflip()
            elif f == 1:
                tile.xflip()
                tile.yflip()
            else:
                tile.yflip()
    raise Exception("tile not found")


def make_puzzle(tiles):
    puzzle = []
    n = int(sqrt(len(tiles)))
    for _ in range(n):
        puzzle.append([None] * n)

    active_tiles = set(tiles)
    puzzle[0][0] = find_corner(tiles)
    active_tiles.remove(puzzle[0][0])
    for i in range(1, n):
        right = puzzle[0][i - 1][:, -1]
        puzzle[0][i] = find_tile_with_same_edge(right, active_tiles)
        active_tiles.remove(puzzle[0][i])

    for i in range(1, n):
        botom = puzzle[i - 1][0][-1, :]
        puzzle[i][0] = find_tile_with_same_edge(
            botom, active_tiles, key=lambda t: t[0, :]
        )
        active_tiles.remove(puzzle[i][0])
    for i in range(1, n):
        for j in range(1, n):
            right = puzzle[i][j - 1][:, -1]
            botom = puzzle[i - 1][j][-1, :]
            puzzle[i][j] = find_tile_with_same_edge(right, active_tiles)
            active_tiles.remove(puzzle[i][j])
            assert puzzle[i][j][0, :] == botom
    return puzzle


def task1(tiles):
    puzzle = make_puzzle(tiles)
    p = 1
    for x in (0, -1):
        for y in (0, -1):
            p *= puzzle[x][y].id
    return p


def is_monster(x, y, coords):
    for coord in coords:
        i, j = coord
        if i <= x < i + MONSTER_X_LEN and j <= y < j + MONSTER_Y_LEN:
            return MONSTER[x - i, y - j] == "#"
    return False


def get_monsters(map_img, map_x_len, map_y_len):
    monsters_coord = []
    for f in range(3):
        for _ in range(4):
            for i in range(map_x_len - MONSTER_X_LEN):
                for j in range(map_y_len - MONSTER_Y_LEN):
                    frag = map_img[i : i + MONSTER_X_LEN, j : j + MONSTER_Y_LEN]
                    if frag.compare(MONSTER):
                        monsters_coord.append((i, j))
            if monsters_coord:
                return monsters_coord
            map_img.rotate()
        if f == 0:
            map_img.xflip()
        elif f == 1:
            map_img.xflip()
            map_img.yflip()
        else:
            map_img.yflip()


def task2(tiles):
    puzzle = make_puzzle(tiles)
    cuted = [[tile[1:-1, 1:-1] for tile in row] for row in puzzle]
    map_data = []
    for row in cuted:
        for i in range(TILE_DIM - 2):
            img_line = ""
            for tile in row:
                img_line += tile[i, :]
            map_data.append(img_line)

    map_x_len = len(map_data)
    map_y_len = len(map_data[0])
    map_img = Image(map_data)

    monster_coords = get_monsters(map_img, map_x_len, map_y_len)

    c = 0
    for i in range(map_x_len):
        for j in range(map_y_len):
            if is_monster(i, j, monster_coords):
                continue
            if map_img[i, j] == "#":
                c += 1

    return c


if __name__ == "__main__":
    main([r.strip() for r in fileinput.input()])
