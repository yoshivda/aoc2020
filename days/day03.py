from math import prod

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return calc_slope(data, 3, 1)


def calc_slope(data, dx, dy):
    return sum(1 for iters in range(len(data) // dy) if data[dy * iters][(dx * iters) % len(data[0])] == "#")


def part_two(data):
    return prod(calc_slope(data, dx, dy) for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])


if __name__ == "__main__":
    print(solve(load_input(3, "small")))
    print(solve(load_input(3)))
