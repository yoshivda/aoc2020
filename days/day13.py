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
    lines = ((index, int(part)) for (index, part) in enumerate(data[1].split(",")) if part != "x")
    time = 0
    step_size = 1
    for index, line in lines:
        while (time + index) % line != 0:
            time += step_size
        step_size *= line
    return time


if __name__ == "__main__":
    print(solve(load_input(13, "small")))

    # PART 2 ONLY
    for i in range(2, 7):
        print(solve(load_input(13, "small" + str(i))))

    print(solve(load_input(13)))
