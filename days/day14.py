import re
from collections import defaultdict
from itertools import product

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    mask = ""
    mem = defaultdict(int)
    for line in data:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        else:
            addr = int(re.match(r"mem\[(\d+)]", line).group(1))
            new_val = bin(int(line.split(" = ")[1]))[2:].zfill(36)
            res = ''.join(str(new_val[i]) if mask[i] == "X" else mask[i] for i in range(36))
            mem[addr] = int(res, 2)
    return sum(mem.values())


def part_two(data):
    mask = ""
    floating = []
    mem = defaultdict(int)
    for line in data:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
            floating = [i for i in range(36) if mask[i] == "X"]
        else:
            addr = bin(int(re.match(r"mem\[(\d+)]", line).group(1)))[2:].zfill(36)
            new_val = int(line.split(" = ")[1])
            res = ["X" if mask[i] == "X" else addr[i] if mask[i] == "0" else mask[i] for i in range(36)]
            if len(floating) == 0:
                mem[int(addr, 2)] = int(''.join(res), 2)
                continue
            for float_values in product([0, 1], repeat=len(floating)):
                for index, value in enumerate(float_values):
                    res[floating[index]] = str(value)
                mem[int(''.join(res), 2)] = new_val
    return sum(mem.values())


if __name__ == "__main__":
    # print(solve(load_input(14, "small")))
    print(solve(load_input(14, "small2")))
    print(solve(load_input(14)))
