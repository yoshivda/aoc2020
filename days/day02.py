from lib import load_input


def solve(data):
    lines = [line.split() for line in data.strip().split("\n")]
    passwords = [(*(map(int, line[0].split("-"))), line[1][0], line[2]) for line in lines]
    return part_one(passwords)
    # return part_two(passwords)


def part_one(passwords):
    return sum(1 for (lower, upper, char, pwd) in passwords if lower <= list(pwd).count(char) <= upper)


def part_two(passwords):
    return sum(1 for (lower, upper, char, pwd) in passwords if (pwd[lower - 1] == char) != (pwd[upper - 1] == char))


if __name__ == "__main__":
    print(solve(load_input(2, "small")))
    print(solve(load_input(2)))
