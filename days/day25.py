from lib import load_input


def transform(subject, loops):
    res = 1
    for _ in range(loops):
        res = (res * subject) % 20201227
    return res


def count_loops(key):
    val = 1
    res = 0
    while val != key:
        val = (val * 7) % 20201227
        res += 1
    return res


def solve(data):
    card, door = map(int, data.splitlines())
    return transform(door, count_loops(card))


if __name__ == "__main__":
    # print(solve(load_input(25, "small")))
    print(solve(load_input(25)))
