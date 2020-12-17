import copy
from itertools import product
from operator import itemgetter

from lib import load_input


def solve(data):
    # return solve_dimensions(data.splitlines(), 3)
    return solve_dimensions(data.splitlines(), 4)


def get_all_positions(mins, maxs):
    res = [(x,) for x in range(mins[0] - 1, maxs[0] + 2)]
    for i in range(1, len(mins)):
        res = {(*prev, x) for prev in res for x in range(mins[i] - 1, maxs[i] + 2)}
    return res


def active_positions_around(pos, active, dimensions):
    res = 0
    for offset in product([-1, 0, 1], repeat=dimensions):
        if offset != (0, ) * dimensions and tuple(map(sum, zip(pos, offset))) in active:
            res += 1

            # Short circuit, we don't care about larger values (saves 15% runtime)
            if res > 3:
                return 4
    return res


def solve_dimensions(data, dimensions):
    active = {(x, y, *(0 for _ in range(dimensions - 2))) for x in range(len(data[0])) for y in range(len(data))
              if data[y][x] == "#"}
    for i in range(6):
        new_active = copy.copy(active)
        mins = [min(active, key=itemgetter(x))[x] for x in range(dimensions)]
        maxs = [max(active, key=itemgetter(x))[x] for x in range(dimensions)]
        for pos in get_all_positions(mins, maxs):
            apa = active_positions_around(pos, active, dimensions)
            if pos in active and not (2 <= apa <= 3):
                new_active.remove(pos)
            elif pos not in active and apa == 3:
                new_active.add(pos)
        active = new_active
    return len(active)


if __name__ == "__main__":
    print(solve(load_input(17, "small")))
    print(solve(load_input(17)))
