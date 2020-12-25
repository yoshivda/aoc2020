from collections import defaultdict
from re import findall

from lib import load_input

directions = {"ne": (.5, -1), "e": (1, 0), "se": (.5, 1), "sw": (-.5, 1), "w": (-1, 0), "nw": (-.5, -1)}


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return len(flip_tiles(data))


def flip_tiles(data):
    tiles = set()
    for line in data:
        c1 = c2 = 0
        for dir in findall(r"[ns]?[we]", line):
            c1, c2 = get_pos(c1, c2, dir)
        if (c1, c2) in tiles:
            tiles.remove((c1, c2))
        else:
            tiles.add((c1, c2))
    return tiles


def get_pos(c1, c2, dir):
    dx, dy = directions[dir]
    return c1 + dx, c2 + dy


def part_two(data):
    tiles = flip_tiles(data)

    for day in range(100):
        pings = defaultdict(int)
        for (c1, c2) in tiles:
            for dc1, dc2 in [get_pos(c1, c2, dir) for dir in directions]:
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
