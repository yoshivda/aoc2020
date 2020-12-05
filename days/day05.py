from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return max(process_seat(line) for line in data)


def process_seat(line):
    row_low = 0
    row_high = 127
    col_low = 0
    col_high = 7

    for char in line:
        row_size = row_high - row_low + 1
        col_size = col_high - col_low + 1
        if char == "F":
            row_high -= row_size // 2
        elif char == "B":
            row_low += row_size // 2
        elif char == "L":
            col_high -= col_size // 2
        elif char == "R":
            col_low += col_size // 2

    seat_id = row_low * 8 + col_low
    return seat_id


def part_two(data):
    seats = {process_seat(line) for line in data}
    for seat in seats:
        if seat - 2 in seats and seat - 1 not in seats:
            return seat - 1
        elif seat + 2 in seats and seat + 1 not in seats:
            return seat + 1
    return -1


if __name__ == "__main__":
    # print(solve(load_input(5, "small")))
    print(solve(load_input(5)))
