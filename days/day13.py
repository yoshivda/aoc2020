import math

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    time = int(data[0])
    orig_time = time
    lines = [int(part) for part in data[1].split(",") if part != "x"]
    while True:
        for line in lines:
            if time % line == 0:
                return line * (time - orig_time)
        time += 1


def part_two(data):
    lines = [int(part) if part != "x" else part for part in data[1].split(",")]
    time = 0
    offset = 0
    found = -1
    cur_lcm = 1
    while True:
        for line in lines:
            if line == "x":
                offset += 1
                continue
            if (time + offset) % line == 0:
                offset += 1
                if offset == len(lines):
                    return time
                elif offset > found:
                    found = offset
                    cur_lcm = lcm(cur_lcm, line)
            else:
                offset = 0
                time += cur_lcm
                break


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


if __name__ == "__main__":
    print(solve(load_input(13, "small")))

    # PART 2 ONLY
    for i in range(2, 7):
        print(solve(load_input(13, "small" + str(i))))

    print(solve(load_input(13)))
