from collections import defaultdict

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return len(flip_tiles(data))


def flip_tiles(data):
    tiles = set()
    for line in data:
        i = c1 = c2 = 0
        while i < len(line):
            if line[i] in "ns":
                dir = line[i:i + 2]
                i += 2
            else:
                dir = line[i]
                i += 1
            c1, c2 = get_pos(c1, c2, dir)
        if (c1, c2) in tiles:
            tiles.remove((c1, c2))
        else:
            tiles.add((c1, c2))
    return tiles


def get_pos(c1, c2, dir):
    if dir == "w":
        return c1 - 1, c2
    elif dir == "e":
        return c1 + 1, c2

    elif dir == "sw":
        if c2 % 2:
            return c1 - 1, c2 + 1
        else:
            return c1, c2 + 1

    elif dir == "se":
        if c2 % 2:
            return c1, c2 + 1
        else:
            return c1 + 1, c2 + 1

    elif dir == "ne":
        if c2 % 2:
            return c1, c2 - 1
        else:
            return c1 + 1, c2 - 1

    elif dir == "nw":
        if c2 % 2:
            return c1 - 1, c2 - 1
        else:
            return c1, c2 - 1


def part_two(data):
    tiles = flip_tiles(data)

    for day in range(100):
        pings = defaultdict(int)
        for (c1, c2) in tiles:
            for dc1, dc2 in [get_pos(c1, c2, dir) for dir in ["w", "e", "ne", "nw", "se", "sw"]]:
                pings[(dc1, dc2)] += 1
        for tile, ping in pings.items():
            if tile in tiles and ping > 2:
                tiles.remove(tile)
            elif tile not in tiles and ping == 2:
                tiles.add(tile)
        tiles = {tile for tile in tiles if pings[tile] > 0}
    return len(tiles)


if __name__ == "__main__":
    print(solve(load_input(24, "small")))
    print(solve(load_input(24)))
