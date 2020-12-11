from collections import defaultdict

from lib import load_input


def solve(data):
    # return part_one([list(line) for line in data.splitlines()])
    return part_two([list(line) for line in data.splitlines()])


def part_one(data):
    occupied_seats = sum(1 for line in data for seat in line if seat == "#")
    diffs = [-1, 0, 1]
    while True:
        new_data = [[c for c in line] for line in data]
        print('\n'.join([''.join(line) for line in data]))
        for y in range(len(data)):
            for x in range(len(data[0])):
                occupied_around = 0
                for dx in diffs:
                    for dy in diffs:
                        if dx == dy == 0:
                            continue
                        if 0 <= x + dx < len(data[0]) and 0 <= y + dy < len(data) \
                                and data[y + dy][x + dx] == "#":
                            occupied_around += 1
                if occupied_around == 0 and data[y][x] == "L":
                    new_data[y][x] = "#"
                elif occupied_around >= 4 and data[y][x] == "#":
                    new_data[y][x] = "L"
        data = new_data
        new_occupied = sum(1 for line in data for seat in line if seat == "#")
        if new_occupied == occupied_seats:
            return new_occupied
        else:
            occupied_seats = new_occupied


def part_two(data):
    occupied_seats = sum(1 for line in data for seat in line if seat == "#")
    diffs = [-1, 0, 1]

    # Precompute visible seats
    visible = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[0])):
            for dx in diffs:
                for dy in diffs:
                    if dx == dy == 0:
                        continue
                    dy_new = dy
                    dx_new = dx
                    while 0 <= x + dx_new < len(data[0]) and 0 <= y + dy_new < len(data) \
                            and data[y + dy_new][x + dx_new] == ".":
                        dx_new += dx
                        dy_new += dy
                    if 0 <= x + dx_new < len(data[0]) and 0 <= y + dy_new < len(data):
                        visible[(x, y)].append((x + dx_new, y + dy_new))

    while True:
        new_data = [[c for c in line] for line in data]
        for y in range(len(data)):
            for x in range(len(data[0])):
                occupied_around = 0
                for vis_x, vis_y in visible[(x, y)]:
                    if data[vis_y][vis_x] == "#":
                        occupied_around += 1
                if occupied_around == 0 and data[y][x] == "L":
                    new_data[y][x] = "#"
                elif occupied_around >= 5 and data[y][x] == "#":
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
