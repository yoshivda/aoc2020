import copy
from collections import defaultdict

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def active_positions_around(x, y, z, levels):
    return sum(1 for dx in (-1, 0, 1)
               for dy in (-1, 0, 1)
               for dz in (-1, 0, 1)
               if not dx == dy == dz == 0
               and levels[(x + dx, y + dy, z + dz)] == "#")


def part_one(data):
    levels = defaultdict(lambda: ".")
    levels.update({(x, y, 0): data[y][x] for x in range(len(data[0])) for y in range(len(data))})
    for i in range(6):
        new_levels = copy.copy(levels)

        for z in range(-i - 1, i + 2):
            for y in range(-i - 1, len(data) + i + 1):
                for x in range(-i - 1, len(data[0]) + i + 1):
                    apa = active_positions_around(x, y, z, levels)
                    if levels[(x, y, z)] == "#" and not (2 <= apa <= 3):
                        new_levels[(x, y, z)] = "."
                    elif levels[(x, y, z)] == "." and apa == 3:
                        new_levels[(x, y, z)] = "#"
        levels = new_levels

    return sum(1 for val in levels.values() if val == "#")


def active_positions_around_w(x, y, z, w, levels):
    return sum(1 for dx in (-1, 0, 1)
               for dy in (-1, 0, 1)
               for dz in (-1, 0, 1)
               for dw in (-1, 0, 1)
               if not dx == dy == dz == dw == 0
               and levels[(x + dx, y + dy, z + dz, w + dw)] == "#")


def part_two(data):
    levels = defaultdict(lambda: ".")
    levels.update({(x, y, 0, 0): data[y][x] for x in range(len(data[0])) for y in range(len(data))})
    for i in range(6):
        new_levels = copy.copy(levels)

        for w in range(-i - 1, i + 2):
            for z in range(-i - 1, i + 2):
                for y in range(-i - 1, len(data) + i + 1):
                    for x in range(-i - 1, len(data[0]) + i + 1):
                        apa = active_positions_around_w(x, y, z, w, levels)
                        if levels[(x, y, z, w)] == "#" and not (2 <= apa <= 3):
                            new_levels[(x, y, z, w)] = "."
                        elif levels[(x, y, z, w)] == "." and apa == 3:
                            new_levels[(x, y, z, w)] = "#"
        levels = new_levels

    return sum(1 for val in levels.values() if val == "#")


if __name__ == "__main__":
    print(solve(load_input(17, "small")))
    print(solve(load_input(17)))
