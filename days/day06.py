from lib import load_input


def solve(data):
    return part_one(data.split("\n\n"))
    # return part_two(data.split("\n\n"))


def part_one(data):
    return sum(len(set(group.replace("\n", ""))) for group in data)


def part_two(data):
    return sum(len(set.intersection(*(set(line) for line in group.splitlines()))) for group in data)


if __name__ == "__main__":
    print(solve(load_input(6, "small")))
    print(solve(load_input(6)))
