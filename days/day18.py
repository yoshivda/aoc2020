from math import prod

from lib import load_input


def solve(data):
    data = data.replace("(", "( ").replace(")", " )")
    # return part_one([line.split() for line in data.splitlines()])
    return part_two([line.split() for line in data.splitlines()])


def evaluate_one(line):
    res = 0
    op = ""
    i = 0
    while i < len(line):
        if line[i] == "+":
            op = "+"
        elif line[i] == "*":
            op = "*"
        elif line[i].isnumeric():
            if op == "+":
                res += int(line[i])
            elif op == "*":
                res *= int(line[i])
            else:
                res = int(line[i])
        elif line[i] == "(":
            orig_pos = i
            brackets = 1
            while brackets > 0:
                i += 1
                if line[i] == "(":
                    brackets += 1
                elif line[i] == ")":
                    brackets -= 1
            part_res = evaluate_one(line[orig_pos + 1: i])
            print(line[orig_pos + 1: i], "=", part_res)
            if op == "+":
                res += part_res
            elif op == "*":
                res *= part_res
            else:
                res = part_res
        i += 1
    return res


def part_one(data):
    res = [evaluate_one(line) for line in data]
    print(res)
    return sum(res)


def evaluate_two(line):
    res = []
    op = ""
    i = 0
    while i < len(line):
        if line[i] == "+":
            op = "+"
        elif line[i] == "*":
            op = "*"
        elif line[i].isnumeric():
            if op == "+":
                res[-1] += int(line[i])
            elif op == "*":
                res.append(int(line[i]))
            else:
                res.append(int(line[i]))
        elif line[i] == "(":
            orig_pos = i
            brackets = 1
            while brackets > 0:
                i += 1
                if line[i] == "(":
                    brackets += 1
                elif line[i] == ")":
                    brackets -= 1
            part_res = evaluate_two(line[orig_pos + 1: i])
            # print(line[orig_pos + 1: i], "=", part_res)
            if op == "+":
                res[-1] += int(part_res)
            else:
                res.append(part_res)
        i += 1
    return prod(res)


def part_two(data):
    res = [evaluate_two(line) for line in data]
    print(res)
    return sum(res)


if __name__ == "__main__":
    print(solve(load_input(18, "small")))
    print(solve(load_input(18)))
