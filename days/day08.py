from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return eval_data(data, 1)


def eval_data(data, part):
    res = 0
    index = 0
    visited = set()
    while index < len(data):
        if index in visited:
            if part == 1:
                return res
            return False
        visited.add(index)
        op, num = data[index].split()
        if op == "acc":
            res += int(num)
            index += 1
        elif op == "jmp":
            index += int(num)
        elif op == "nop":
            index += 1
    return res


def part_two(data):
    for i in range(len(data)):
        if "nop" in data[i]:
            new_data = data[:i] + [data[i].replace("nop", "jmp")] + data[i + 1:]
            if res := eval_data(new_data, 2):
                return res
        elif "jmp" in data[i]:
            new_data = data[:i] + [data[i].replace("jmp", "nop")] + data[i+1:]
            if res := eval_data(new_data, 2):
                return res
    return False


if __name__ == "__main__":
    print(solve(load_input(8, "small")))
    print(solve(load_input(8)))
