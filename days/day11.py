from collections import defaultdict

from lib import load_input


def solve(data):
    return part_one([list(line) for line in data.splitlines()])
    # return part_two([list(line) for line in data.splitlines()])


def part_one(data):
    return compute(data, 1)


def part_two(data):
    return compute(data, 2)


# Precomputes all visible seats from each position
def get_visible_seats(data, part):
    visible = defaultdict(list)
    diffs = [-1, 0, 1]
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == ".":
                continue
            for dx in diffs:
                for dy in diffs:
                    if dx == 0 and dy == 0:
                        continue
                    x_new = x + dx
                    y_new = y + dy
                    while part == 2 and 0 <= x_new < len(data[0]) and 0 <= y_new < len(data) \
                            and data[y_new][x_new] == ".":
                        x_new += dx
                        y_new += dy
                    if 0 <= x_new < len(data[0]) and 0 <= y_new < len(data) and data[y_new][x_new] != ".":
                        visible[(x, y)].append((x_new, y_new))
    return visible


def compute(data, part):
    occupied_seats = sum(1 for line in data for seat in line if seat == "#")
    visible = get_visible_seats(data, part).items()
    iters = 0
    while True:
        iters += 1
        new_data = [[c for c in line] for line in data]
        for ((x, y), vis) in visible:
            occupied_around = sum(1 for vis_x, vis_y in vis if data[vis_y][vis_x] == "#")
            if occupied_around == 0 and data[y][x] == "L":
                new_data[y][x] = "#"
            elif occupied_around >= 3 + part and data[y][x] == "#":
                new_data[y][x] = "L"
        data = new_data
        new_occupied = sum(1 for line in data for seat in line if seat == "#")
        if new_occupied == occupied_seats:
            return new_occupied
        else:
            occupied_seats = new_occupied


if __name__ == "__main__":
    print(solve(load_input(11, "small")))
    print(solve(load_input(11)))
