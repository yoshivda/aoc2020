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


def evaluate_one(line):
    return eval(re.sub(r"(\d+)", r"Int(\1)", line).replace("*", "-"))


def part_one(data):
    return sum(evaluate_one(line).val for line in data)


def evaluate_two(line):
    return eval(re.sub(r"(\d+)", r"Int(\1)", line).replace("*", "-").replace("+", "/"))


def part_two(data):
    return sum(evaluate_two(line).val for line in data)


if __name__ == "__main__":
    print(solve(load_input(18, "small")))
    print(solve(load_input(18)))
