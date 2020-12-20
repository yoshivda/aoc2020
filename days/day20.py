import re
from math import prod, sqrt

from lib import load_input


def solve(data):
    # return part_one(data.split("\n\n"))
    return part_two(data.split("\n\n"))


def part_one(data):
    tiles = {int(block.splitlines()[0].split()[1][:-1]): block.splitlines()[1:] for block in data}
    sides = dict()
    for id, tile in tiles.items():
        tile_sides = set()
        tile_sides.add(tile[0])
        tile_sides.add(tile[0][::-1])
        tile_sides.add(tile[-1])
        tile_sides.add(tile[-1][::-1])
        tile_sides.add(''.join(line[0] for line in tile))
        tile_sides.add(''.join(line[0] for line in tile)[::-1])
        tile_sides.add(''.join(line[-1] for line in tile))
        tile_sides.add(''.join(line[-1] for line in tile)[::-1])
        sides[id] = tile_sides

    matching_sides = dict()
    for id1, sides1 in sides.items():
        matches = []
        for id2, sides2 in sides.items():
            if id1 == id2:
                continue
            if len(sides1.intersection(sides2)) > 0:
                matches.append(id2)
        matching_sides[id1] = matches
    return prod(id for id, sides in matching_sides.items() if len(sides) == 2)


def part_two(data):
    tiles = {int(block.splitlines()[0].split()[1][:-1]): block.splitlines()[1:] for block in data}
    tile_size = len(data[0].splitlines()[1])
    sides = dict()
    for id, tile in tiles.items():
        tile_sides = dict()
        tile_sides.update({"0": tile[0]})
        tile_sides.update({"0r": tile[0][::-1]})
        tile_sides.update({"2": tile[-1]})
        tile_sides.update({"2r": tile[-1][::-1]})
        tile_sides.update({"1": ''.join(line[-1] for line in tile)})
        tile_sides.update({"1r": ''.join(line[-1] for line in tile)[::-1]})
        tile_sides.update({"3": ''.join(line[0] for line in tile)})
        tile_sides.update({"3r": ''.join(line[0] for line in tile)[::-1]})
        sides[id] = tile_sides

    matching_sides = dict()
    for id1, sides1 in sides.items():
        matches = []
        for id2, sides2 in sides.items():
            if id1 == id2:
                continue
            for side_num1, value1 in sides1.items():
                for side_num2, value2 in sides2.items():
                    if value1 == value2:
                        matches.append([id2, side_num1, side_num2])
        matching_sides[id1] = matches

    m_size = round(sqrt(len(tiles)))
    corners = [id for id, match in matching_sides.items() if len(match) == 4]
    edges = [id for id, match in matching_sides.items() if len(match) == 6]
    centers = [id for id, match in matching_sides.items() if len(match) == 8]
    matrix = [[None for _ in range(m_size)] for _ in range(m_size)]

    prev = corners[0]
    matrix[0][0] = prev
    sides = sorted({int(s[1][0]) for s in matching_sides[prev]})
    if sides == [0, 3]:
        rotate = 2
        next_side = 3
    else:
        rotate = (2 - max(sides)) % 4
        next_side = min(sides)
    for _ in range(rotate):
        tiles[prev] = [''.join(tiles[prev][i][j] for i in range(len(tiles[prev]) - 1, -1, -1)) for j in range(len(tiles[prev]))]
    matrix[0][1] = (next(int(s[0]) for s in matching_sides[prev] if s[1] == str(next_side)))
    tiles[matrix[0][1]] = rotate_flip_tile(tiles[matrix[0][1]], tiles[matrix[0][0]], 0)
    used = {prev, matrix[0][1]}
    prev = matrix[0][1]
    for i in range(2, m_size):
        if i == m_size - 1:
            next_id, src_side, target_side = next(
                s for s in matching_sides[prev] if s[0] not in used and s[0] in corners)
        else:
            next_id, src_side, target_side = next(s for s in matching_sides[prev]
                                                  if s[0] not in used and s[0] in edges)
        used.add(next_id)
        matrix[0][i] = next_id

        tiles[next_id] = rotate_flip_tile(tiles[next_id], tiles[prev], 0)
        prev = next_id
    for i in range(1, m_size):
        for j in range(m_size):
            if j == 0 or j == m_size - 1:
                if i == m_size - 1:
                    next_id = next(s[0] for s in matching_sides[matrix[i - 1][j]]
                                   if s[0] not in used and s[0] in corners)
                else:
                    next_id = next(s[0] for s in matching_sides[matrix[i - 1][j]]
                                   if s[0] not in used and s[0] in edges)
            elif i == m_size - 1:
                next_id = next(s[0] for s in matching_sides[matrix[i - 1][j]]
                               if s[0] not in used and s[0] in edges)
            else:
                next_id = next(s[0] for s in matching_sides[matrix[i - 1][j]]
                               if s[0] not in used and s[0] in centers)
            matrix[i][j] = next_id
            used.add(next_id)
            tiles[next_id] = rotate_flip_tile(tiles[next_id], tiles[matrix[i-1][j]], 1)

    for _, tile in tiles.items():
        del tile[0]
        del tile[-1]
        for index, row in enumerate(tile):
            tile[index] = row[1:-1]
    tile_size -= 2

    monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #"]

    matrix_text = [''.join(tiles[matrix[j][i]][line] for i in range(m_size)) for j in range(m_size) for line in range(tile_size)]
    total_tag = sum(line.count("#") for line in matrix_text)
    monster_tag = sum(line.count("#") for line in monster)

    res = [''.join(tiles[matrix[j][i]][line] for i in range(m_size)) for j in range(m_size) for line in range(tile_size)]

    for _ in range(4):
        # Rotate
        res = [''.join(res[i][j] for i in range(len(res) - 1, -1, -1)) for j in range(len(res))]
        if times := count_monsters(res):
            return total_tag - monster_tag * times
        else:
            # Horizontal flip
            new_res = [line[::-1] for line in res]
            if times := count_monsters(new_res):
                return total_tag - monster_tag * times
    return 0


def count_monsters(text):
    monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #"]
    monster_indices = [[m.start() for m in re.finditer('#', line)] for line in monster]
    count = 0
    for i in range(len(text) - 2):
        for j in range(len(text[0])):
            if j + len(monster[0]) - 1 < len(text[0]):
                if all(text[i + dy][j + dx] == "#" for dy in range(len(monster)) for dx in monster_indices[dy]):
                    count += 1
    return count


def rotate_flip_tile(tile, target_tile, dir):
    def matches(tile, target_tile, dir):
        if dir == 1:
            return target_tile[-1] == tile[0]
        else:
            return [line[0] for line in tile] == [line[-1] for line in target_tile]

    res = tile
    for _ in range(4):
        # Rotate
        res = [''.join(res[i][j] for i in range(len(res) - 1, -1, -1)) for j in range(len(res))]
        if matches(res, target_tile, dir):
            return res
        else:
            # Horizontal flip
            new_res = [line[::-1] for line in res]
            if matches(new_res, target_tile, dir):
                return new_res


if __name__ == "__main__":
    print(solve(load_input(20, "small")))
    print(solve(load_input(20)))
