from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    pos_x = 0
    pos_y = 0
    dirs = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
    cur_dir = "E"
    for line in data:
        if line[0] in "NESW":
            pos_x += dirs[line[0]][0] * int(line[1:])
            pos_y += dirs[line[0]][1] * int(line[1:])
        elif line[0] == "L":
            cur_dir = "NESW"[("NESW".index(cur_dir) - (int(line[1:]) // 90)) % 4]
        elif line[0] == "R":
            cur_dir = "NESW"[("NESW".index(cur_dir) + (int(line[1:]) // 90)) % 4]
        elif line[0] == "F":
            pos_x += dirs[cur_dir][0] * int(line[1:])
            pos_y += dirs[cur_dir][1] * int(line[1:])
    return abs(pos_x) + abs(pos_y)


def part_two(data):
    pos_x = 0
    pos_y = 0
    way_x = 10
    way_y = -1
    dirs = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
    for line in data:
        if line[0] in "NESW":
            way_x += dirs[line[0]][0] * int(line[1:])
            way_y += dirs[line[0]][1] * int(line[1:])
        elif line[0] == "L":
            way_x, way_y = rotate(way_x, way_y, 360-int(line[1:]))
        elif line[0] == "R":
            way_x, way_y = rotate(way_x, way_y, int(line[1:]))
        elif line[0] == "F":
            pos_x += way_x * int(line[1:])
            pos_y += way_y * int(line[1:])
    return abs(pos_x) + abs(pos_y)


def rotate(way_x, way_y, degrees):
    if degrees == 90:
        return -way_y, way_x
    elif degrees == 180:
        return -way_x, -way_y
    return way_y, -way_x


if __name__ == "__main__":
    print(solve(load_input(12, "small")))
    print(solve(load_input(12)))
