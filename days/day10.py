from lib import load_input


def solve(data):
    # return part_one([int(line) for line in data.splitlines()])
    return part_two([int(line) for line in data.splitlines()])


def part_one(data):
    data.append(0)
    data.sort()
    return sum(1 for i in range(len(data) - 1) if data[i + 1] - data[i] == 1) * \
           (sum(1 for i in range(len(data) - 1) if data[i + 1] - data[i] == 3) + 1)


def part_two(data):
    data.append(0)
    data.append(max(data) + 3)
    data.sort()

    mem = [0] * len(data)
    mem[0] = 1
    for i in range(1, len(data)):
        for j in range(1, 4):
            if 0 <= i - j < len(data) and data[i] - data[i - j] <= 3:
                mem[i] += mem[i - j]
    return mem[-1]


if __name__ == "__main__":
    print(solve(load_input(10, "small")))
    print(solve(load_input(10, "medium")))
    print(solve(load_input(10)))
