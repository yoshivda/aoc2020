from itertools import combinations
from lib import load_input


def solve(data):
    nums = [int(line) for line in data.splitlines()]
    # return part_one(nums)
    return part_two(nums)


def part_one(nums):
    return next(i * j for i, j in combinations(nums, 2) if i + j == 2020)


def part_two(nums):
    return next(i * j * k for i, j, k in combinations(nums, 3) if i + j + k == 2020)


if __name__ == "__main__":
    print(solve(load_input(1)))
