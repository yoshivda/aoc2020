from lib import load_input
import re


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


class Int:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Int(self.val + other.val)

    def __sub__(self, other):
        return Int(self.val * other.val)

    def __truediv__(self, other):
        return Int(self.val + other.val)


def part_one(data):
    return sum(eval(re.sub(r"(\d+)", r"Int(\1)", line).replace("*", "-")).val for line in data)


def part_two(data):
    return sum(eval(re.sub(r"(\d+)", r"Int(\1)", line).replace("*", "-").replace("+", "/")).val for line in data)


if __name__ == "__main__":
    print(solve(load_input(18, "small")))
    print(solve(load_input(18)))
