from lib import load_input


def solve(data):
    # return part_one([int(num) for num in data.splitlines()])
    return part_two([int(num) for num in data.splitlines()])


def sum_in_preamble(num, preamble):
    for attempt in preamble:
        if num - attempt in preamble:
            return True
    return False


def part_one(data):
    if len(data) == 20:
        pre = 5
    else:
        pre = 25

    for start in range(len(data)):
        preamble = set(data[start:start+pre])
        if not sum_in_preamble(data[start + pre], preamble):
            return data[start+pre]
    return -1


def part_two(data):
    ans = part_one(data)

    for size in range(2, len(data)):
        for i in range(len(data) - size):
            sublist = data[i:i+size]
            if sum(sublist) == ans:
                return min(sublist) + max(sublist)
            if sum(sublist) > ans:
                break


if __name__ == "__main__":
    print(solve(load_input(9, "small")))
    print(solve(load_input(9)))
