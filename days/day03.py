from math import prod

from lib import load_input


def solve(data):
    # return part_one(input.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return calc_slope(data, 1, 3)


def calc_slope(data, row_offset, col_offset):
    cnt = 0
    row = 0
    col = 0
    while row < len(data):
        if col >= len(data[0]):
            col -= len(data[0])
        if data[row][col] == "#":
            cnt += 1
        row += row_offset
        col += col_offset
    return cnt


def part_two(data):
    return prod(calc_slope(data, row, col) for col, row in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])


if __name__ == "__main__":
    print(solve(load_input(3, "small")))
    print(solve(load_input(3)))
