from math import prod

from lib import load_input


def solve(data):
    # return part_one(data.split("\n\n"))
    return part_two(data.split("\n\n"))


def part_one(data):
    return sum(int(num) for line in data[2].splitlines()[1:] for num in line.split(",")
               if not any(min <= int(num) <= max
                          for _, values in get_field_bounds(data).items()
                          for (min, max) in values))


def is_valid(fields, line):
    for num in line.split(","):
        if not any(min <= int(num) <= max for _, values in fields.items() for (min, max) in values):
            return False
    return True


def get_field_bounds(data):
    fields = dict()
    for line in data[0].splitlines():
        name, values = line.split(":")
        bounds = []
        for value in values.split(" or "):
            min, max = value.split("-")
            bounds.append((int(min), int(max)))
        fields[name] = bounds
    return fields


def part_two(data):
    fields = get_field_bounds(data)

    possible = {i: {name for name in fields.keys()} for i in range(len(data[1].splitlines()[1].split(",")))}
    for line in data[2].splitlines()[1:]:
        if not is_valid(fields, line):
            continue
        for i, num in enumerate(line.split(",")):
            for name, values in fields.items():
                if not any(min <= int(num) <= max for (min, max) in values):
                    possible[i] -= {name}

    res_names = dict()
    while len(res_names.keys()) != len(fields.keys()):
        for index, vals in possible.items():
            if len(vals) == 1:
                name = vals.pop()
                res_names[name] = index
                for val in possible.values():
                    val -= {name}

    indices = []
    for name, index in res_names.items():
        if name.startswith("departure"):
            indices.append(index)

    your_ticket = data[1].splitlines()[1].split(",")
    return prod(int(your_ticket[i]) for i in indices)


if __name__ == "__main__":
    print(solve(load_input(16, "small")))
    print(solve(load_input(16)))
