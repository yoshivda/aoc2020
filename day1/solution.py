from itertools import combinations


def solve(filename):
    with open(filename) as f:
       nums = [int(line) for line in f]
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
    print(solve("input.txt"))
