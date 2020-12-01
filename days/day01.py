from itertools import combinations
from lib import load_input


def solve(input):
    nums = [int(line) for line in input.strip().split("\n")]
    # return part_one(nums)
    return part_two(nums)


def part_one(nums):
    for i, j in combinations(nums, 2):
        if i + j == 2020:
            return i * j


def part_two(nums):
    for i, j, k in combinations(nums, 3):
        if i + j + k == 2020:
            return i * j * k


if __name__ == "__main__":
    print(solve(load_input(1)))
