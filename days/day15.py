from collections import defaultdict
from lib import load_input


def solve(data):
    # return part_one([int(line) for line in data.split(",")])
    return part_two([int(line) for line in data.split(",")])


def calc_until(data, turn):
    ages = defaultdict(list)
    ages.update({v: [k] for k, v in enumerate(data)})
    res = data[-1]
    for i in range(len(data), turn):
        if len(ages[res]) > 1:
            res = ages[res][-1] - ages[res][-2]
        else:
            res = 0
        ages[res].append(i)
    return res


def part_one(data):
    return calc_until(data, 2020)


def part_two(data):
    return calc_until(data, 30000000)


if __name__ == "__main__":
    print(solve(load_input(15, "small")))
    print(solve(load_input(15)))
