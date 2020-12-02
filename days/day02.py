from itertools import combinations
from lib import load_input


def solve(input):
    passes = [line.split() for line in input.strip().split("\n")]
    # return part_one(passes)
    return part_two(passes)


def part_one(passes):
    cnt = 0
    for limits, letter, phrase in passes:
        lower, upper = limits.split("-")
        if int(lower) <= list(phrase).count(letter[0]) <= int(upper):
            cnt += 1
    return cnt


def part_two(passes):
    cnt = 0
    for limits, letter, phrase in passes:
        letter = letter[0]
        lower, upper = limits.split("-")
        if (phrase[int(lower) - 1] == letter) != (phrase[int(upper) - 1] == letter):
            cnt += 1
    return cnt


if __name__ == "__main__":
    print(solve(load_input(2)))
