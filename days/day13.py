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
    line_index = 0
    step_size = 1
    while True:
        line = lines[line_index]
        if line == "x":
            line_index += 1
            continue
        if (time + line_index) % line == 0:
            line_index += 1
            if line_index == len(lines):
                return time
            step_size *= line
        else:
            time += step_size


if __name__ == "__main__":
    print(solve(load_input(13, "small")))

    # PART 2 ONLY
    for i in range(2, 7):
        print(solve(load_input(13, "small" + str(i))))

    print(solve(load_input(13)))
