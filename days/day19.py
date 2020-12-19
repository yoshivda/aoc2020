from lib import load_input


def solve(data):
    # return part_one(data.split("\n\n"))
    return part_two(data.split("\n\n"))


def parse_data(data):
    rules = dict()
    for line in data[0].splitlines():
        rules[int(line.split(":")[0])] = [[int(x) if isinstance(x, str) and x.isnumeric() else x for x in part.split()]
                                          for part in line.split(":")[1].replace('"', '').split("|")]
    return data[1].splitlines(), rules


def is_valid(line, rules, nums):
    if len(nums) == 0:
        return len(line) == 0
    num = nums[0]
    rest_nums = nums[1:]
    rule = rules[num]
    if len(rule) == 1 and len(rule[0]) == 1 and rule[0][0] == "a" or rule[0][0] == "b":
        return line.startswith(rule[0][0]) and is_valid(line[1:], rules, rest_nums)
    else:
        return any(is_valid(line, rules, option + rest_nums) for option in rule)


def count_valid(lines, rules):
    return sum(1 for line in lines if is_valid(line, rules, [0]))


def part_one(data):
    return count_valid(*parse_data(data))


def part_two(data):
    lines, rules = parse_data(data)
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    return count_valid(lines, rules)


if __name__ == "__main__":
    print(solve(load_input(19, "small2")))
    print(solve(load_input(19)))
