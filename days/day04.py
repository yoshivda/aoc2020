import re
from math import prod

from lib import load_input


def solve(data):
    # return part_one(data.split("\n\n"))
    return part_two(data.split("\n\n"))


def part_one(data):
    return sum(1 for passport in data if all(field in passport for field in ("ecl:", "pid:", "eyr:", "hcl:", "byr:",
                                                                             "iyr:", "hgt:")))


def part_two(data):
    cnt = 0
    for passport in data:
        valid = True
        fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        for field in passport.split():
            name, value = field.split(":")
            if name == "cid":
                continue
            if name not in fields:
                valid = False
                break
            if is_valid(name, value):
                fields.remove(name)
            else:
                valid = False
                break
        if valid and len(fields) == 0:
            cnt += 1
    return cnt


def is_valid(name, value):
    if name == "byr":
        return value.isnumeric() and 1920 <= int(value) <= 2002
    elif name == "iyr":
        return value.isnumeric() and 2010 <= int(value) <= 2020
    elif name == "eyr":
        return value.isnumeric() and 2020 <= int(value) <= 2030
    elif name == "hgt":
        if value[-2:] == "cm":
            return value[:-2].isnumeric() and 150 <= int(value[:-2]) <= 193
        elif value[-2:] == "in":
            return value[:-2].isnumeric() and 59 <= int(value[:-2]) <= 76
        return False
    elif name == "hcl":
        return len(value) == 7 and bool(re.match("#[0-9a-f]{6}", value))
    elif name == "ecl":
        return value in "amb blu brn gry grn hzl oth".split()
    elif name == "pid":
        return len(value) == 9 and value.isnumeric()
    else:
        return False


if __name__ == "__main__":
    # print(solve(load_input(4, "2invalid")))
    # print(solve(load_input(4, "2valid")))
    print(solve(load_input(4)))
